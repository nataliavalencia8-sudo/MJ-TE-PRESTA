# pf_Algoritmos
# Módulo: modDevoluciones
# Sistema: MJ TE PRESTA

import os
from datetime import date
from clsPrestamos import cargar_prestamos, actualizar_estado_prestamo, prestamos_activos_por_usuario
from clsUsuarios import buscar_usuario
from clsItems import buscar_item, actualizar_disponibilidad

def registrar_devolucion():
    print("\n  ╔══════════════════════════╗")
    print("  ║  REGISTRAR DEVOLUCIÓN    ║")
    print("  ╚══════════════════════════╝")

    documento = input("  Documento del usuario: ").strip()
    usuario = buscar_usuario(documento)
    if not usuario:
        print("  ❌ Usuario no encontrado.")
        return

    activos = prestamos_activos_por_usuario(documento)
    if not activos:
        print(f"  ❌ {usuario.nombre} {usuario.apellido} no tiene préstamos activos.")
        return

    print(f"\n  Préstamos activos de {usuario.nombre} {usuario.apellido}:")
    for i, p in enumerate(activos, 1):
        item = buscar_item(p.item_id)
        nombre_item = item.nombre if item else p.item_id
        print(f"    {i}. [{p.prestamo_id}] {nombre_item} — {p.dias_transcurridos()} días")

    while True:
        try:
            sel = int(input("\n  Seleccione el préstamo a devolver: ")) - 1
            if 0 <= sel < len(activos):
                break
            print("  ❌ Opción inválida.")
        except ValueError:
            print("  ❌ Ingrese un número.")

    prestamo = activos[sel]
    item = buscar_item(prestamo.item_id)
    fecha_devolucion = date.today().strftime("%Y-%m-%d")

    actualizar_estado_prestamo(prestamo.prestamo_id, "devuelto")
    actualizar_disponibilidad(prestamo.item_id, True)

    # Generar certificado en texto plano
    nombre_archivo = f"data/certificado_{usuario.nombre}_{fecha_devolucion}_{prestamo.item_id}.txt"
    os.makedirs("data", exist_ok=True)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("     CERTIFICADO DE DEVOLUCIÓN\n")
        f.write("         MJ TE PRESTA\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"  Fecha de devolución : {fecha_devolucion}\n")
        f.write(f"  Usuario             : {usuario.nombre} {usuario.apellido}\n")
        f.write(f"  Documento           : {usuario.documento}\n")
        f.write(f"  Ítem devuelto       : {item.nombre if item else prestamo.item_id}\n")
        f.write(f"  ID Ítem             : {prestamo.item_id}\n")
        f.write(f"  ID Préstamo         : {prestamo.prestamo_id}\n")
        f.write(f"  Fecha de préstamo   : {prestamo.fecha_inicio}\n")
        f.write(f"  Días transcurridos  : {prestamo.dias_transcurridos()}\n\n")
        f.write("  Se certifica que el ítem fue devuelto en las\n")
        f.write("  condiciones acordadas.\n\n")
        f.write("=" * 50 + "\n")

    print(f"\n  ✅ Devolución registrada exitosamente.")
    print(f"  📄 Certificado generado: {nombre_archivo}")
