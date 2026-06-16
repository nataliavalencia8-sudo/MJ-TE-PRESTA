import os

# pf_Algoritmos
# Archivo principal: main.py
# Sistema: MJ TE PRESTA

# Las siguientes funciones/clases se definen en otras celdas y están en el ámbito global
# por lo que no necesitan ser importadas de esta manera.
# from clsUsuarios import registrar_usuario, listar_usuarios
# from clsItems import registrar_item, listar_items
# from clsPrestamos import registrar_prestamo, consultar_prestamos
# from modDevoluciones import registrar_devolucion
# from modAdministrador import menu_administrador

def mostrar_menu():
    print("\n")
    print("  ─────────────────────────────────────────────")
    print("  ███╗   ███╗      ██╗    ████████╗███████╗")
    print("  ████╗ ████║      ██║    ╚══██╔══╝██╔════╝")
    print("  ██╔████╔██║      ██║       ██║   █████╗  ")
    print("  ██║╚██╔╝██║██    ██║       ██║   ██╔══╝  ")
    print("  ██║ ╚═╝ ██║╚██████╔╝       ██║   ███████╗")
    print("  ╚═╝     ╚═╝ ╚═════╝        ╚═╝   ╚══════╝")
    print("                 P R E S T A")
    print("  ─────────────────────────────────────────────")
    print("       Bienvenido a MJ TE PRESTA")
    print("  ─────────────────────────────────────────────")
    print("    1. Registrar Usuario")
    print("    2. Registrar Ítem")
    print("    3. Registrar Préstamo")
    print("    4. Registrar Devolución")
    print("    5. Consultar Ítems con más de 30 días")
    print("    6. Consultar Artículos Prestados")
    print("    7. Administrador")
    print("    8. Salir")
    print("  ─────────────────────────────────────────────")

def main():
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_item()
        elif opcion == "3":
            registrar_prestamo()
        elif opcion == "4":
            registrar_devolucion()
        elif opcion == "5":
            # from clsPrestamos import prestamos_con_mas_de_30_dias # Removido, ya está global
            # from clsUsuarios import buscar_usuario # Removido, ya está global
            # from clsItems import buscar_item # Removido, ya está global
            vencidos = prestamos_con_mas_de_30_dias()
            if not vencidos:
                print("\n  ✅ No hay ítems con más de 30 días prestados.")
            else:
                print(f"\n  🔴 Ítems con más de 30 días ({len(vencidos)}):")
                for p in vencidos:
                    u = buscar_usuario(p.documento_usuario)
                    it = buscar_item(p.item_id)
                    print(f"\n  - {it.nombre if it else p.item_id} | "
                          f"Usuario: {u.nombre+' '+u.apellido if u else p.documento_usuario} | "
                          f"Días: {p.dias_transcurridos()}")
        elif opcion == "6":
            consultar_prestamos()
        elif opcion == "7":
            menu_administrador()
        elif opcion == "8":
            print("\n  ¡Hasta luego! 👋\n")
            break
        else:
            print("\n  ❌ Opción inválida. Intente de nuevo.")

        input("\n  Presione Enter para continuar...")

if __name__ == "__main__":
    main()
