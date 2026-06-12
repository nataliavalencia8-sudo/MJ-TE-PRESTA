# pf_Algoritmos
# Clase: clsUsuarios
# Sistema: MJ TE PRESTA

import csv
import os

ARCHIVO_USUARIOS = "data/usuarios.csv"

class clsUsuarios:
    def __init__(self, nombre, apellido, documento, correo, plazo):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.plazo = int(plazo)

    def __str__(self):
        return (f"  Nombre   : {self.nombre} {self.apellido}\n"
                f"  Documento: {self.documento}\n"
                f"  Correo   : {self.correo}\n"
                f"  Plazo    : {self.plazo} días")


# ---------- Validaciones ----------

def validar_nombre(valor):
    if len(valor) < 3:
        return False, "Debe tener mínimo 3 caracteres."
    if any(c.isdigit() for c in valor):
        return False, "No puede contener números."
    return True, ""

def validar_documento(valor):
    if not valor.isdigit():
        return False, "Solo se permiten números."
    if not (3 <= len(valor) <= 15):
        return False, "Debe tener entre 3 y 15 dígitos."
    return True, ""

def validar_correo(valor):
    if "@" not in valor or ".com" not in valor:
        return False, "Debe contener '@' y '.com'."
    return True, ""

def validar_plazo(valor):
    if valor not in ["5", "10", "15", "30"]:
        return False, "Solo se permiten valores: 5, 10, 15 o 30."
    return True, ""


# ---------- Persistencia ----------

def guardar_usuario(usuario):
    os.makedirs("data", exist_ok=True)
    existe = os.path.exists(ARCHIVO_USUARIOS)
    with open(ARCHIVO_USUARIOS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["nombre", "apellido", "documento", "correo", "plazo"])
        writer.writerow([usuario.nombre, usuario.apellido, usuario.documento,
                         usuario.correo, usuario.plazo])

def cargar_usuarios():
    usuarios = []
    if not os.path.exists(ARCHIVO_USUARIOS):
        return usuarios
    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            usuarios.append(clsUsuarios(fila["nombre"], fila["apellido"],
                                        fila["documento"], fila["correo"], fila["plazo"]))
    return usuarios

def buscar_usuario(documento):
    for u in cargar_usuarios():
        if u.documento == documento:
            return u
    return None


# ---------- Menú ----------

def registrar_usuario():
    print("\n  ╔══════════════════════════╗")
    print("  ║    REGISTRAR USUARIO     ║")
    print("  ╚══════════════════════════╝")

    while True:
        nombre = input("  Nombre    : ").strip()
        ok, msg = validar_nombre(nombre)
        if ok: break
        print(f"  ❌ {msg}")

    while True:
        apellido = input("  Apellido  : ").strip()
        ok, msg = validar_nombre(apellido)
        if ok: break
        print(f"  ❌ {msg}")

    while True:
        documento = input("  Documento : ").strip()
        ok, msg = validar_documento(documento)
        if not ok:
            print(f"  ❌ {msg}"); continue
        if buscar_usuario(documento):
            print("  ❌ Ya existe un usuario con ese documento."); continue
        break

    while True:
        correo = input("  Correo    : ").strip()
        ok, msg = validar_correo(correo)
        if ok: break
        print(f"  ❌ {msg}")

    while True:
        plazo = input("  Plazo (5/10/15/30 días): ").strip()
        ok, msg = validar_plazo(plazo)
        if ok: break
        print(f"  ❌ {msg}")

    u = clsUsuarios(nombre, apellido, documento, correo, plazo)
    guardar_usuario(u)
    print(f"\n  ✅ Usuario '{nombre} {apellido}' registrado exitosamente.")

def listar_usuarios():
    print("\n  ╔══════════════════════════╗")
    print("  ║    LISTADO DE USUARIOS   ║")
    print("  ╚══════════════════════════╝")
    usuarios = cargar_usuarios()
    if not usuarios:
        print("  No hay usuarios registrados.")
        return
    for i, u in enumerate(usuarios, 1):
        print(f"\n  [{i}]\n{u}")
