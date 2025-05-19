import json
from datetime import datetime
from typing import List, Dict, Optional
from modules.utils import (
    cargar_archivo_json,
    guardar_archivo_json,
    mostrar_mensaje,
    validar_entero
)
from modules.usuarios import Usuario
from modules.productos import guardar_productos, mostrar_inventario_admin

ARCHIVO_ADMINS = "data/admins.json"
CODIGO_MAESTRO = "270207"  # En un sistema real, esto debería estar en variables de entorno

def validar_email(email: str) -> bool:
    """Valida el formato de un email"""
    import re
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

class Administrador:
    """Clase que representa a un administrador del sistema"""
    
    def __init__(self, id_admin: int, usuario: str, contrasena: str, nombre: str, email: str):
        self.id = id_admin
        self.usuario = usuario
        self.contrasena = Usuario.encriptar_contrasena(contrasena)
        self.nombre = nombre
        self.email = email
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convierte el objeto administrador a diccionario"""
        return {
            "id": self.id,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "nombre": self.nombre,
            "email": self.email,
            "fecha_registro": self.fecha_registro
        }

def cargar_admins() -> List[Dict]:
    """Carga los administradores desde el archivo JSON"""
    return cargar_archivo_json(ARCHIVO_ADMINS, [])

def guardar_admins(admins: List[Dict]) -> bool:
    """Guarda los administradores en el archivo JSON"""
    return guardar_archivo_json(ARCHIVO_ADMINS, admins)

def autenticar_admin(usuario: str, contrasena: str) -> bool:
    """Autentica a un administrador"""
    admins = cargar_admins()
    if not admins:
        mostrar_mensaje("No hay administradores registrados", "error")
        return False
    
    contrasena_encriptada = Usuario.encriptar_contrasena(contrasena)
    
    for admin in admins:
        if admin["usuario"] == usuario:
            if admin["contrasena"] == contrasena_encriptada:
                return True
            mostrar_mensaje("Contraseña incorrecta", "error")
            return False
    
    mostrar_mensaje("Usuario admin no encontrado", "error")
    return False

def verificar_codigo_maestro() -> bool:
    """Valida el código maestro para operaciones críticas"""
    intentos = 3
    while intentos > 0:
        codigo = input("Ingrese el código maestro: ")
        if codigo == CODIGO_MAESTRO:
            return True
        intentos -= 1
        mostrar_mensaje(f"Código incorrecto. Intentos restantes: {intentos}", "error")
    return False

def agregar_admin() -> bool:
    """Registra un nuevo administrador con validación de datos"""
    if not verificar_codigo_maestro():
        mostrar_mensaje("Acceso denegado")
        return False
    
    admins = cargar_admins()
    print("\n=== REGISTRO DE ADMINISTRADOR ===")
    
    try:
        id_admin = validar_entero(input("ID único numérico: "))
        if id_admin is None:
            mostrar_mensaje("El ID debe ser un número válido", "error")
            return False
            
        if any(admin.get("id") == id_admin for admin in admins):
            mostrar_mensaje("Este ID ya está registrado", "error")
            return False
    except ValueError:
        mostrar_mensaje("El ID debe ser un número", "error")
        return False
    
    usuario = input("Usuario admin: ").strip()
    if any(admin["usuario"] == usuario for admin in admins):
        mostrar_mensaje("Este usuario ya existe", "error")
        return False
    
    contrasena = input("Contraseña (mínimo 8 caracteres): ").strip()
    if len(contrasena) < 8:
        mostrar_mensaje("La contraseña debe tener al menos 8 caracteres", "error")
        return False
    
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        mostrar_mensaje("El nombre no puede estar vacío", "error")
        return False
    
    email = input("Email institucional: ").strip()
    if not validar_email(email):
        mostrar_mensaje("Email no válido", "error")
        return False
    
    nuevo_admin = Administrador(id_admin, usuario, contrasena, nombre, email)
    admins.append(nuevo_admin.to_dict())
    
    if guardar_admins(admins):
        mostrar_mensaje("Administrador registrado exitosamente", "exito")
        return True
    
    mostrar_mensaje("Error al guardar el administrador", "error")
    return False

def cargar_premios() -> Dict:
    """Carga los premios desde el archivo JSON"""
    try:
        premios = cargar_archivo_json("data/premios.json", {})
        if not premios:  # Si no hay premios, crea unos iniciales
            premios = {
                "Café Turco": {"puntos_requeridos": 35, "stock": 50},
                "Coca-Cola": {"puntos_requeridos": 30, "stock": 50},
                "Tinto Tradicional": {"puntos_requeridos": 5, "stock": 50},
                "Tinto Campesino": {"puntos_requeridos": 6, "stock": 50},
                "Café Americano": {"puntos_requeridos": 5, "stock": 50},
                "Café con Leche": {"puntos_requeridos": 6, "stock": 50},
                "Cappuccino Tradicional": {"puntos_requeridos": 7, "stock": 50},
                "Latte Frío (Vainilla Canela)": {"puntos_requeridos": 8, "stock": 50},
                "Mocca Frío": {"puntos_requeridos": 8, "stock": 50},
                "Espresso Frío": {"puntos_requeridos": 6, "stock": 50},
                "Chai Frío (Tradicional / Vainilla)": {"puntos_requeridos": 7, "stock": 50},
                "Té Matcha con Miel Frío": {"puntos_requeridos": 9, "stock": 50},
                "Nevado (varios sabores)": {"puntos_requeridos": 10, "stock": 50},
                "Almojábana": {"puntos_requeridos": 4, "stock": 50},
                "Arepa Rellena de Queso": {"puntos_requeridos": 5, "stock": 50},
                "Croissant Integral Multicereal": {"puntos_requeridos": 5, "stock": 50},
                "Muffin de Yogurt y Arándanos": {"puntos_requeridos": 5, "stock": 50},
                "Brownie": {"puntos_requeridos": 6, "stock": 50},
                "Cheesecake de Fresa": {"puntos_requeridos": 7, "stock": 50},
                "Café Especial": {"puntos_requeridos": 7, "stock": 50}
            }
            guardar_premios(premios)
        return premios
    except Exception as e:
        mostrar_mensaje(f"Error al cargar premios: {str(e)}", "error")
        return {}

def guardar_premios(premios: Dict) -> bool:
    """Guarda los premios en el archivo JSON"""
    return guardar_archivo_json("data/premios.json", premios)

def mostrar_menu_premios(premios: Dict):
    """Muestra la lista de premios en formato de tabla"""
    print("\n=== GESTIÓN DE PREMIOS ===")
    print("{:<5} {:<30} {:<20} {:<10}".format(
        "No.", "Premio", "Puntos Requeridos", "Stock"))
    print("-" * 70)
    
    for idx, (nombre, detalles) in enumerate(premios.items(), 1):
        stock = "Ilimitado" if detalles.get("stock", 0) == float('inf') else detalles.get("stock", 0)
        print("{:<5} {:<30} {:<20} {:<10}".format(
            idx, nombre, detalles["puntos_requeridos"], stock))

def gestionar_premios(premios: Dict):
    """Menú para gestionar los premios del sistema"""
    while True:
        mostrar_menu_premios(premios)
        
        print("\nOpciones:")
        print("1. Agregar nuevo premio")
        print("2. Editar premio existente")
        print("3. Eliminar premio")
        print("4. Volver al menú anterior")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:  # Agregar premio
                try:
                    nombre = input("Nombre del premio: ").strip()
                    if nombre in premios:
                        mostrar_mensaje("Este premio ya existe", "error")
                        continue
                        
                    puntos = int(input("Puntos requeridos: "))
                    stock = input("Stock inicial (dejar vacío para ilimitado): ").strip()
                    
                    nuevo_premio = {
                        "puntos_requeridos": puntos,
                        "stock": float('inf') if not stock else int(stock)
                    }
                    
                    premios[nombre] = nuevo_premio
                    guardar_premios(premios)
                    mostrar_mensaje("Premio agregado exitosamente", "exito")
                    
                except ValueError:
                    mostrar_mensaje("Debe ingresar valores numéricos válidos", "error")
                    
            elif opcion == 2:  # Editar premio
                try:
                    num = int(input("Número del premio a editar: "))
                    premios_list = list(premios.items())
                    
                    if 1 <= num <= len(premios_list):
                        nombre = premios_list[num-1][0]
                    print(f"\nEditando premio: {nombre}")
                        
                    nuevos_puntos = input(f"Nuevos puntos ({premios[nombre]['puntos_requeridos']}): ").strip()
                    if nuevos_puntos:
                        premios[nombre]["puntos_requeridos"] = int(nuevos_puntos)
                            
                        nuevo_stock = input(f"Nuevo stock ({premios[nombre].get('stock', 'Ilimitado')}): ").strip()
                        if nuevo_stock:
                            premios[nombre]["stock"] = float('inf') if not nuevo_stock else int(nuevo_stock)
                        
                        guardar_premios(premios)
                        mostrar_mensaje("Premio actualizado exitosamente", "exito")
                    else:
                        mostrar_mensaje("Número de premio inválido", "error")
                        
                except ValueError:
                    mostrar_mensaje("Debe ingresar valores numéricos válidos", "error")
                    
            elif opcion == 3:  # Eliminar premio
                try:
                    num = int(input("Número del premio a eliminar: "))
                    premios_list = list(premios.items())
                    
                    if 1 <= num <= len(premios_list):
                        nombre = premios_list[num-1][0]
                        if input(f"¿Confirmar eliminar '{nombre}'? (s/n): ").lower() == 's':
                            del premios[nombre]
                            guardar_premios(premios)
                            mostrar_mensaje("Premio eliminado exitosamente", "exito")
                    else:
                        mostrar_mensaje("Número de premio inválido", "error")
                        
                except ValueError:
                    mostrar_mensaje("Debe ingresar un número válido", "error")
                    
            elif opcion == 4:  # Volver
                break
                
            else:
                mostrar_mensaje("Opción no válida", "error")
                
        except ValueError:
            mostrar_mensaje("Debe ingresar un número válido", "error")

def menu_administrador(productos: List[Dict], premios: Dict):
    """Menú principal para administradores"""
    while True:
        mostrar_inventario_admin(productos)
        
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Agregar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Actualizar stock")
        print("5. Gestionar premios")
        print("6. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:
                try:
                    nuevo_producto = {
                        "nombre": input("Nombre del producto: ").strip(),
                        "precio": float(input("Precio (COP): ")),
                        "puntos": int(input("Puntos a otorgar: ")),
                        "stock": int(input("Stock inicial: "))
                    }
                    productos.append(nuevo_producto)
                    guardar_productos(productos)
                    mostrar_mensaje("\nProducto agregado exitosamente", "exito")
                except ValueError:
                    mostrar_mensaje("\nError: Debe ingresar valores numéricos válidos", "error")
            
            elif opcion == 2:
                try:
                    idx = int(input("Número de producto a editar: ")) - 1
                    if 0 <= idx < len(productos):
                        # Editar campos
                        nuevo_nombre = input(f"Nuevo nombre ({productos[idx]['nombre']}): ").strip()
                        if nuevo_nombre:
                            productos[idx]["nombre"] = nuevo_nombre
                        
                        nuevo_precio = input(f"Nuevo precio ({productos[idx]['precio']}): ").strip()
                        if nuevo_precio:
                            productos[idx]["precio"] = float(nuevo_precio)
                        
                        nuevos_puntos = input(f"Nuevos puntos ({productos[idx]['puntos']}): ").strip()
                        if nuevos_puntos:
                            productos[idx]["puntos"] = int(nuevos_puntos)
                        
                        guardar_productos(productos)
                        mostrar_mensaje("\nProducto actualizado exitosamente", "exito")
                    else:
                        mostrar_mensaje("\nNúmero de producto inválido", "error")
                except ValueError:
                    mostrar_mensaje("\nError: Debe ingresar valores numéricos válidos", "error")
                    
            elif opcion == 3:
                try:
                    idx = int(input("Número de producto a eliminar: ")) - 1
                    if 0 <= idx < len(productos):
                        confirmacion = input(f"¿Eliminar '{productos[idx]['nombre']}'? (s/n): ").lower()
                        if confirmacion == 's':
                            productos.pop(idx)
                            guardar_productos(productos)
                            mostrar_mensaje("\nProducto eliminado exitosamente", "exito")
                    else:
                        mostrar_mensaje("\nNúmero de producto inválido", "error")
                except ValueError:
                    mostrar_mensaje("\nDebe ingresar un número válido", "error")
                    
            elif opcion == 4:
                try:
                    idx = int(input("Número de producto a actualizar: ")) - 1
                    if 0 <= idx < len(productos):
                        nuevo_stock = int(input(f"Nuevo stock para '{productos[idx]['nombre']}' (actual: {productos[idx].get('stock', 0)}): "))
                        productos[idx]["stock"] = nuevo_stock
                        guardar_productos(productos)
                        mostrar_mensaje("\nStock actualizado exitosamente", "exito")
                    else:
                        mostrar_mensaje("\nNúmero de producto inválido", "error")
                except ValueError:
                    mostrar_mensaje("\nDebe ingresar un número válido", "error")
                    
            elif opcion == 5:
                gestionar_premios(premios)
                
            elif opcion == 6:
                break
                
            else:
                mostrar_mensaje("\nOpción no válida", "error")
                
        except ValueError:
            mostrar_mensaje("\nDebe ingresar un número válido", "error")
