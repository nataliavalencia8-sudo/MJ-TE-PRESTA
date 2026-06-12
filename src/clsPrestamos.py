# pf_Algoritmos
# Clase: clsPrestamos
# Sistema: MJ TE PRESTA

import csv
import os
from datetime import datetime, date

ARCHIVO_PRESTAMOS = "data/prestamos.csv"


class clsPrestamos:
    def __init__(self, prestamo_id, documento_usuario, item_id, fecha_inicio, plazo, estado="activo"):
        self.prestamo_id = prestamo_id
        self.documento_usuario = documento_usuario
        self.item_id = item_id
        self.fecha_inicio = fecha_inicio  # string "YYYY-MM-DD"
        self.plazo = int(plazo)
        self.estado = estado  # activo, devuelto, vendido

    def dias_transcurridos(self):
        inicio = datetime.strptime(self.fecha_inicio, "%Y-%m-%d").date()
        return (date.today() - inicio).days

    def __str__(self):
        dias = self.dias_transcurridos()
        return (f"  ID Préstamo : {self.prestamo_id}\n"
                f"  Usuario     : {self.documento_usuario}\n"
                f"  Ítem        : {self.item_id}\n"
                f"  Fecha inicio: {self.fecha_inicio}\n"
                f"  Plazo       : {self.plazo} días\n"
                f"  Días transcurridos: {dias}\n"
                f"  Estado      : {self.estado}")


# ---------- Persistencia ----------

def generar_id_prestamo():
    prestamos = cargar_prestamos()
    return f"PR{len(prestamos) + 1:04d}"

def guardar_prestamo(prestamo):
    os.makedirs("data", exist_ok=True)
    existe = os.path.exists(ARCHIVO_PRESTAMOS)
    with open(ARCHIVO_PRESTAMOS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["prestamo_id", "documento_usuario", "item_id",
                             "fecha_inicio", "plazo", "estado"])
        writer.writerow([prestamo.prestamo_id, prestamo.documento_usuario,
                         prestamo.item_id, prestamo.fecha_inicio,
                         prestamo.plazo, prestamo.estado])

def cargar_prestamos():
    prestamos = []
    if not os.path.exists(ARCHIVO_PRESTAMOS):
        return prestamos
    with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            p = clsPrestamos(fila["prestamo_id"], fila["documento_usuario"],
                             fila["item_id"], fila["fecha_inicio"],
                             fila["plazo"], fila["estado"])
            prestamos.append(p)
    return prestamos

def actualizar_estado_prestamo(prestamo_id, nuevo_estado):
    prestamos = cargar_prestamos()
    with open(ARCHIVO_PRESTAMOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["prestamo_id", "documento_usuario", "item_id",
                         "fecha_inicio", "plazo", "estado"])
        for p in prestamos:
            if p.prestamo_id == prestamo_id:
                p.estado = nuevo_estado
            writer.writerow([p.prestamo_id, p.documento_usuario, p.item_id,
                             p.fecha_inicio, p.plazo, p.estado])

def prestamos_activos_por_usuario(documento):
    return [p for p in cargar_prestamos()
            if p.documento_usuario == documento and p.estado == "activo"]

def prestamos_con_mas_de_30_dias():
    return [p for p in cargar_prestamos()
            if p.estado == "activo" and p.dias_transcurridos() > 30]

def prestamos_con_alerta():
    return [p for p in cargar_prestamos()
            if p.estado == "activo" and p.dias_transcurridos() >= 20]


# ---------- Menú ----------

def registrar_prestamo():
    from clsUsuarios import buscar_usuario
    from clsItems import buscar_item, listar_items, actualizar_disponibilidad

    print("\n  ╔══════════════════════════╗")
    print("  ║   REGISTRAR PRÉSTAMO     ║")
    print("  ╚══════════════════════════╝")

    # Verificar usuario
    documento = input("  Documento del usuario: ").strip()
    usuario = buscar_usuario(documento)
    if not usuario:
        print("  ❌ Usuario no encontrado. Debe registrarlo primero.")
        return

    print(f"\n  ✅ Usuario encontrado: {usuario.nombre} {usuario.apellido}")

    # Mostrar ítems disponibles
    listar_items(solo_disponibles=True)

    # Seleccionar ítem
    item_id = input("\n  Ingrese el ID del ítem a prestar: ").strip().upper()
    item = buscar_item(item_id)
    if not item:
        print("  ❌ Ítem no encontrado.")
        return
    if not item.disponible:
        print("  ❌ Ese ítem ya está prestado.")
        return

    # Crear préstamo
    prestamo_id = generar_id_prestamo()
    fecha_inicio = date.today().strftime("%Y-%m-%d")
    prestamo = clsPrestamos(prestamo_id, documento, item_id, fecha_inicio, usuario.plazo)

    guardar_prestamo(prestamo)
    actualizar_disponibilidad(item_id, False)

    print(f"\n  ✅ Préstamo registrado exitosamente.")
    print(f"     ID Préstamo : {prestamo_id}")
    print(f"     Ítem        : {item.nombre} ({item_id})")
    print(f"     Plazo       : {usuario.plazo} días")
    print(f"     Fecha inicio: {fecha_inicio}")

def consultar_prestamos():
    from clsUsuarios import buscar_usuario
    from clsItems import buscar_item

    print("\n  ╔══════════════════════════════════╗")
    print("  ║   ARTÍCULOS PRESTADOS (por días) ║")
    print("  ╚══════════════════════════════════╝")

    prestamos = [p for p in cargar_prestamos() if p.estado == "activo"]
    if not prestamos:
        print("  No hay préstamos activos.")
        return

    # Ordenar por días transcurridos (mayor a menor)
    prestamos.sort(key=lambda p: p.dias_transcurridos(), reverse=True)

    for p in prestamos:
        usuario = buscar_usuario(p.documento_usuario)
        item = buscar_item(p.item_id)
        nombre_u = f"{usuario.nombre} {usuario.apellido}" if usuario else p.documento_usuario
        nombre_i = item.nombre if item else p.item_id
        alerta = " ⚠️ ALERTA +20 días" if p.dias_transcurridos() >= 20 else ""
        vencido = " 🔴 VENCIDO +30 días" if p.dias_transcurridos() > 30 else ""
        print(f"\n  Préstamo : {p.prestamo_id}")
        print(f"  Usuario  : {nombre_u}")
        print(f"  Ítem     : {nombre_i}")
        print(f"  Días     : {p.dias_transcurridos()}{alerta}{vencido}")
