# pf_Algoritmos
# Clase: clsItems
# Sistema: MJ TE PRESTA

import csv
import os

ARCHIVO_ITEMS = "data/items.csv"

CATEGORIAS = {
    "1": ("Videojuegos", "VJ"),
    "2": ("Libros", "LB"),
    "3": ("Música y video", "MV"),
    "4": ("Herramientas", "HE"),
    "5": ("Dinero", "DI"),
    "6": ("Misceláneo y varios", "MI")
}

ESTADOS = {
    "1": "Excelente",
    "2": "Bueno",
    "3": "Regular",
    "4": "Malo"
}


class clsItems:
    def __init__(self, item_id, nombre, categoria, precio, estado):
        self.item_id = item_id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.estado = estado
        self.disponible = True

    def __str__(self):
        disp = "Disponible" if self.disponible else "Prestado"
        return (f"  ID       : {self.item_id}\n"
                f"  Nombre   : {self.nombre}\n"
                f"  Categoría: {self.categoria}\n"
                f"  Precio   : ${self.precio:,.0f}\n"
                f"  Estado   : {self.estado}\n"
                f"  Situación: {disp}")


# ---------- Generador de ID ----------

def generar_id(prefijo):
    items = cargar_items()
    ids_existentes = [it.item_id for it in items if it.item_id.startswith(prefijo)]
    numero = len(ids_existentes) + 1
    return f"{prefijo}{numero:03d}"


# ---------- Persistencia ----------

def guardar_item(item):
    os.makedirs("data", exist_ok=True)
    existe = os.path.exists(ARCHIVO_ITEMS)
    with open(ARCHIVO_ITEMS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["item_id", "nombre", "categoria", "precio", "estado", "disponible"])
        writer.writerow([item.item_id, item.nombre, item.categoria,
                         item.precio, item.estado, item.disponible])

def cargar_items():
    items = []
    if not os.path.exists(ARCHIVO_ITEMS):
        return items
    with open(ARCHIVO_ITEMS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            it = clsItems(fila["item_id"], fila["nombre"], fila["categoria"],
                          fila["precio"], fila["estado"])
            it.disponible = fila["disponible"] == "True"
            items.append(it)
    return items

def actualizar_disponibilidad(item_id, disponible):
    items = cargar_items()
    with open(ARCHIVO_ITEMS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["item_id", "nombre", "categoria", "precio", "estado", "disponible"])
        for it in items:
            if it.item_id == item_id:
                it.disponible = disponible
            writer.writerow([it.item_id, it.nombre, it.categoria,
                             it.precio, it.estado, it.disponible])

def buscar_item(item_id):
    for it in cargar_items():
        if it.item_id == item_id:
            return it
    return None


# ---------- Menú ----------

def registrar_item():
    print("\n  ╔══════════════════════════╗")
    print("  ║      REGISTRAR ÍTEM      ║")
    print("  ╚══════════════════════════╝")

    # Nombre
    while True:
        nombre = input("  Nombre del ítem (mín. 3 caracteres): ").strip()
        if len(nombre) >= 3:
            break
        print("  ❌ El nombre debe tener mínimo 3 caracteres.")

    # Categoría
    print("\n  Categorías disponibles:")
    for k, (cat, _) in CATEGORIAS.items():
        print(f"    {k}. {cat}")
    while True:
        opcion = input("  Seleccione categoría (1-6): ").strip()
        if opcion in CATEGORIAS:
            categoria, prefijo = CATEGORIAS[opcion]
            break
        print("  ❌ Opción inválida.")

    # Precio
    while True:
        try:
            precio = float(input("  Precio de compra: $").strip())
            if precio >= 0:
                break
            print("  ❌ El precio no puede ser negativo.")
        except ValueError:
            print("  ❌ Ingrese un valor numérico.")

    # Estado (lógica difusa)
    print("\n  Estado del ítem:")
    for k, est in ESTADOS.items():
        print(f"    {k}. {est}")
    while True:
        opcion_est = input("  Seleccione estado (1-4): ").strip()
        if opcion_est in ESTADOS:
            estado = ESTADOS[opcion_est]
            break
        print("  ❌ Opción inválida.")

    item_id = generar_id(prefijo)
    item = clsItems(item_id, nombre, categoria, precio, estado)
    guardar_item(item)
    print(f"\n  ✅ Ítem registrado con ID: {item_id}")

def listar_items(solo_disponibles=False):
    titulo = "ÍTEMS DISPONIBLES" if solo_disponibles else "TODOS LOS ÍTEMS"
    print(f"\n  ╔══════════════════════════╗")
    print(f"  ║  {titulo:<24}║")
    print(f"  ╚══════════════════════════╝")
    items = cargar_items()
    if solo_disponibles:
        items = [it for it in items if it.disponible]
    if not items:
        print("  No hay ítems registrados.")
        return
    for i, it in enumerate(items, 1):
        print(f"\n  [{i}]\n{it}")
