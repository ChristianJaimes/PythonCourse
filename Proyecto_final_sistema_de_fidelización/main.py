from modules.usuarios import cargar_usuarios, registrar_usuario_con_correo, iniciar_sesion, menu_usuario
from modules.productos import cargar_productos, guardar_productos
from modules.admin import menu_administrador, autenticar_admin, agregar_admin, cargar_admins
from modules.utils import mostrar_mensaje
import json
import os

# Configuración
PREMIOS_FILE = "data/premios.json"

def cargar_premios():
    """Carga los premios desde archivo JSON"""
    try:
        os.makedirs(os.path.dirname(PREMIOS_FILE), exist_ok=True)
        if not os.path.exists(PREMIOS_FILE):
            premios_iniciales = {
                "Café Turco": {"puntos_requeridos": 35, "stock": 50},
                "Coca-Cola": {"puntos_requeridos": 30, "stock": 50},
                "Tinto Tradicional": {"puntos_requeridos": 25, "stock": 50},
                "Tinto Campesino": {"puntos_requeridos": 16, "stock": 50},
                "Café Americano": {"puntos_requeridos": 15, "stock": 50},
                "Café con Leche": {"puntos_requeridos": 10, "stock": 50},
                "Cappuccino Tradicional": {"puntos_requeridos": 37, "stock": 50},
                "Latte Frío (Vainilla Canela)": {"puntos_requeridos": 38, "stock": 50},
                "Mocca Frío": {"puntos_requeridos": 28, "stock": 50},
                "Espresso Frío": {"puntos_requeridos": 6, "stock": 50},
                "Chai Frío (Tradicional / Vainilla)": {"puntos_requeridos": 17, "stock": 50},
                "Té Matcha con Miel Frío": {"puntos_requeridos": 19, "stock": 50},
                "Nevado (varios sabores)": {"puntos_requeridos": 10, "stock": 50},
                "Almojábana": {"puntos_requeridos": 14, "stock": 50},
                "Arepa Rellena de Queso": {"puntos_requeridos": 15, "stock": 50},
                "Croissant Integral Multicereal": {"puntos_requeridos": 15, "stock": 50},
                "Muffin de Yogurt y Arándanos": {"puntos_requeridos": 25, "stock": 50},
                "Brownie": {"puntos_requeridos": 16, "stock": 50},
                "Cheesecake de Fresa": {"puntos_requeridos": 17, "stock": 50},
                "Café Especial": {"puntos_requeridos": 17, "stock": 50}
            }
            with open(PREMIOS_FILE, 'w') as f:
                json.dump(premios_iniciales, f, indent=4)
            return premios_iniciales
        
        with open(PREMIOS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        mostrar_mensaje(f"Error al cargar premios: {str(e)}", tipo="error")
        return {}

def inicializar_sistema():
    """Función para crear el primer administrador si no existe"""
    admins = cargar_admins()
    if not admins:
        print("\n=== CONFIGURACIÓN INICIAL ===")
        print("No hay administradores registrados. Creando uno inicial...")
        agregar_admin()

def main():
    # Inicializar sistema
    inicializar_sistema()
    
    # Cargar datos
    usuarios = cargar_usuarios()
    productos = cargar_productos()
    premios = cargar_premios()

    while True:
        
        print("\n=== Sistema de Fidelización Juan Valdez ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Modo Administrador")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario_con_correo(usuarios)
            
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                menu_usuario(usuario, usuarios, productos, premios)
                
        elif opcion == "3":
            
            print("\n--- Autenticación Administrador ---")
            usuario_admin = input("Usuario admin: ").strip()
            contrasena_admin = input("Contraseña: ").strip()
            
            if autenticar_admin(usuario_admin, contrasena_admin):
                mostrar_mensaje(f"\nBienvenido {usuario_admin}", tipo="exito")
                menu_administrador(productos, premios)
            else:
                mostrar_mensaje("\nCredenciales incorrectas. Acceso denegado.", tipo="error")
                
        elif opcion == "4":
            mostrar_mensaje("\nGracias por usar el sistema. Hasta luego.", tipo="info")
            break
            
        else:
            mostrar_mensaje("\nOpción inválida. Por favor ingrese 1, 2, 3 o 4.", tipo="error")

main()
