# pf_Algoritmos
# Módulo: modAdministrador
# Sistema: MJ TE PRESTA

import os
from datetime import date
from clsPrestamos import cargar_prestamos, prestamos_con_mas_de_30_dias, actualizar_estado_prestamo
from clsUsuarios import cargar_usuarios, buscar_usuario
from clsItems import buscar_item, actualizar_disponibilidad

# Credenciales de administrador
ADMINS = {
    "admin": "mj2026",
    "cindy": "udea123"
}

def login_administrador():
    print("\n  ╔══════════════════════════╗")
    print("  ║      ADMINISTRADOR       ║")
    print("  ╚══════════════════════════╝")
    usuario = input("  Usuario: ").strip()
    clave   = input("  Clave  : ").strip()
    if ADMINS.get(usuario) == clave:
        print("  ✅ Acceso concedido.")
        return True
    print("  ❌ Usuario o clave incorrectos.")
    return False

def menu_administrador():
    if not login_administrador():
        return
    while True:
        print("\n  ╔══════════════════════════════╗")
        print("  ║     MENÚ ADMINISTRADOR       ║")
        print("  ╠══════════════════════════════╣")
        print("  ║  1. Total préstamos          ║")
        print("  ║  2. Total devoluciones       ║")
        print("  ║  3. Total ventas             ║")
        print("  ║  4. Total dinero recaudado   ║")
        print("  ║  5. Lista de usuarios        ║")
        print("  ║  6. Mayor/menor prestamista  ║")
        print("  ║  7. Generar ventas >30 días  ║")
        print("  ║  8. Volver al menú principal ║")
        print("  ╚══════════════════════════════╝")
        op = input("  Seleccione: ").strip()

        if op == "1":
            total = len(cargar_prestamos())
            print(f"\n  📊 Total de préstamos registrados: {total}")

        elif op == "2":
            devueltos = [p for p in cargar_prestamos() if p.estado == "devuelto"]
            print(f"\n  📦 Total de ítems devueltos: {len(devueltos)}")

        elif op == "3":
            vendidos = [p for p in cargar_prestamos() if p.estado == "vendido"]
            print(f"\n  💰 Total de ventas realizadas: {len(vendidos)}")

        elif op == "4":
            vendidos = [p for p in cargar_prestamos() if p.estado == "vendido"]
            total_pago = 0
            for p in vendidos:
                item = buscar_item(p.item_id)
                if item:
                    subtotal = item.precio
                    total_pago += subtotal * 1.23
            print(f"\n  💵 Total recaudado (con impuesto 23%): ${total_pago:,.0f}")

        elif op == "5":
            usuarios = cargar_usuarios()
            print(f"\n  👥 Lista de usuarios ({len(usuarios)} total):")
            for u in usuarios:
                print(f"\n{u}")

        elif op == "6":
            usuarios = cargar_usuarios()
            prestamos = cargar_prestamos()
            if not usuarios:
                print("  No hay usuarios registrados.")
                continue
            conteo = {}
            for u in usuarios:
                conteo[u.documento] = sum(1 for p in prestamos if p.documento_usuario == u.documento)
            max_doc = max(conteo, key=conteo.get)
            min_doc = min(conteo, key=conteo.get)
            u_max = buscar_usuario(max_doc)
            u_min = buscar_usuario(min_doc)
            print(f"\n  🏆 Mayor cantidad de préstamos: {u_max.nombre} {u_max.apellido} ({conteo[max_doc]})")
            print(f"  📉 Menor cantidad de préstamos: {u_min.nombre} {u_min.apellido} ({conteo[min_doc]})")

        elif op == "7":
            generar_ventas()

        elif op == "8":
            break
        else:
            print("  ❌ Opción inválida.")

def generar_ventas():
    vencidos = prestamos_con_mas_de_30_dias()
    if not vencidos:
        print("\n  ✅ No hay préstamos con más de 30 días.")
        return

    print(f"\n  🔴 Se encontraron {len(vencidos)} préstamo(s) con más de 30 días:")
    for p in vencidos:
        usuario = buscar_usuario(p.documento_usuario)
        item = buscar_item(p.item_id)
        if not usuario or not item:
            continue

        subtotal = item.precio
        impuesto = subtotal * 0.23
        total = subtotal + impuesto
        fecha = date.today().strftime("%Y-%m-%d")

        nombre_archivo = f"data/factura_{usuario.nombre}_{p.item_id}.txt"
        os.makedirs("data", exist_ok=True)
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write("        FACTURA DE VENTA\n")
            f.write("         MJ TE PRESTA\n")
            f.write("=" * 50 + "\n\n")
            f.write("  MOTIVACIÓN:\n")
            f.write(f"  El ítem '{item.nombre}' fue prestado el {p.fecha_inicio}\n")
            f.write(f"  y no fue devuelto tras {p.dias_transcurridos()} días.\n")
            f.write(f"  Según el acuerdo, superar 30 días implica\n")
            f.write(f"  la compra obligatoria del artículo.\n\n")
            f.write("-" * 50 + "\n")
            f.write(f"  Fecha de factura : {fecha}\n")
            f.write(f"  Cliente          : {usuario.nombre} {usuario.apellido}\n")
            f.write(f"  Documento        : {usuario.documento}\n")
            f.write(f"  Ítem             : {item.nombre}\n")
            f.write(f"  ID Ítem          : {p.item_id}\n")
            f.write(f"  ID Préstamo      : {p.prestamo_id}\n")
            f.write("-" * 50 + "\n")
            f.write(f"  Subtotal         : ${subtotal:>12,.0f}\n")
            f.write(f"  Impuesto (23%)   : ${impuesto:>12,.0f}\n")
            f.write(f"  TOTAL            : ${total:>12,.0f}\n")
            f.write("=" * 50 + "\n")

        actualizar_estado_prestamo(p.prestamo_id, "vendido")
        actualizar_disponibilidad(p.item_id, True)
        print(f"\n  ✅ Factura generada: {nombre_archivo}")
        print(f"     Total a pagar: ${total:,.0f}")
