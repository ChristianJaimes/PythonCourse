# main.py
from comprador import menu_comprador
from vendedor import menu_vendedor
from utils import cargar_usuarios

def login():
    usuarios = cargar_usuarios()
    username = input("Usuario: ")
    password = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print(f"¡Bienvenido {username}!")
            return usuario
    print("Usuario o contraseña incorrectos.")
    return None

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = login()
            if usuario:
                if usuario["rol"] == "comprador":
                    menu_comprador(usuario["username"])
                elif usuario["rol"] == "vendedor":
                    menu_vendedor(usuario["username"])
            else:
                print("No se pudo iniciar sesión.")
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
