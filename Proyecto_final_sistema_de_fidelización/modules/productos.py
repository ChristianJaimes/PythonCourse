from typing import List, Dict, Optional
from modules.utils import (
    cargar_archivo_json,
    guardar_archivo_json,
    mostrar_mensaje,
    validar_entero
)

ARCHIVO_PRODUCTOS = "data/productos.json"

def mostrar_inventario_admin(productos: List[Dict]) -> None:
    """Muestra el inventario de productos en formato de tabla para administradores"""
    if not productos:
        mostrar_mensaje("No hay productos registrados.", "info")
        return
    
    print("\n================== INVENTARIO JUAN VALDEZ =====================")
    print("| No. | PRODUCTO                     | PRECIO    | PUNTOS  | STOCK |")
    print("|-----|------------------------------|-----------|---------|-------|")
    
    for idx, producto in enumerate(productos, 1):
        stock = producto.get("stock", 0)
        precio_formateado = "${:,.0f}".format(producto["precio"])
        nombre_producto = (producto["nombre"][:25] + "...") if len(producto["nombre"]) > 25 else producto["nombre"]
        
        print(f"| {idx:<3} | {nombre_producto:<28} | {precio_formateado:>9} | {producto['puntos']:>7} | {stock:>5} |")

def cargar_productos() -> List[Dict]:
    """Carga los productos desde el archivo JSON"""
    productos = cargar_archivo_json(ARCHIVO_PRODUCTOS, [])
    
    # Inicializar campos obligatorios si no existen
    for producto in productos:
        producto.setdefault("stock", 0)
        producto.setdefault("puntos", 0)
    
    return productos

def guardar_productos(productos: List[Dict]) -> bool:
    """Guarda la lista de productos en el archivo JSON"""
    return guardar_archivo_json(ARCHIVO_PRODUCTOS, productos)

def mostrar_menu_canje(usuario: str, usuarios: Dict, premios: Dict) -> bool:
    """Muestra el menú para canjear puntos por premios"""
    if not premios:
        mostrar_mensaje("No hay premios disponibles para canjear.", "info")
        return False
        
    puntos_usuario = usuarios[usuario]["puntos"]
    print(f"\n=== CANJE DE PUNTOS ===")
    print(f"Tienes {puntos_usuario} puntos disponibles\n")
    
    print("{:<15} {:<35} {:<15}".format("Opción", "Premio", "Puntos requeridos"))
    print("-" * 65)
    
    premios_disponibles = list(premios.items())
    for idx, (nombre_premio, detalles) in enumerate(premios_disponibles, 1):
        print("{:<15} {:<35} {:<15}".format(
            idx, 
            nombre_premio, 
            detalles['puntos_requeridos']
        ))
    
    opcion = input("\nSeleccione el premio a canjear (0 para cancelar): ")
    opcion_num = validar_entero(opcion)
    
    if opcion_num is None:
        mostrar_mensaje("Debe ingresar un número válido", "error")
        return False
        
    if opcion_num == 0:
        return False
        
    if 1 <= opcion_num <= len(premios_disponibles):
        premio_seleccionado = premios_disponibles[opcion_num-1][0]
        puntos_requeridos = premios_disponibles[opcion_num-1][1]['puntos_requeridos']
        
        if puntos_usuario >= puntos_requeridos:
            usuarios[usuario]['puntos'] -= puntos_requeridos
            mostrar_mensaje(f"\n¡Canje exitoso! Has obtenido: {premio_seleccionado}", "exito")
            verificar_descuento(usuario, usuarios)
            return True
        else:
            mostrar_mensaje("\nNo tienes suficientes puntos para este premio", "error")
    else:
        mostrar_mensaje("\nOpción inválida", "error")
    
    return False

def aplicar_descuento(precio: float, usuario: str, usuarios: Dict) -> float:
    """Aplica descuento del 10% si está disponible"""
    if usuarios[usuario].get("descuento_activo", False):
        descuento = precio * 0.10
        precio_final = precio - descuento
        usuarios[usuario]["descuento_activo"] = False
        mostrar_mensaje(f"¡Descuento del 10% aplicado! Ahorraste ${descuento:,.2f}")
        return precio_final
    return precio

def verificar_descuento(usuario: str, usuarios: Dict) -> None:
    """Activa descuento al alcanzar 100 puntos"""
    if usuarios[usuario]["puntos"] >= 100 and not usuarios[usuario].get("descuento_activo", False):
        usuarios[usuario]["descuento_activo"] = True
        mostrar_mensaje("\n¡Felicidades! Has ganado un 10% de descuento para tu próxima compra")

def mostrar_menu_compra(usuario: str, usuarios: Dict, productos: List[Dict]) -> bool:
    """Muestra el menú de compra de productos"""
    if not productos:
        mostrar_mensaje("No hay productos disponibles para comprar.", "info")
        return False
        
    print("\n========================= TIENDA JUAN VALDEZ =========================")
    print("{:<4} {:<30} {:<12} {:<10} {:<10}".format("No.", "PRODUCTO", "PRECIO", "PUNTOS", "STOCK"))
    print("-" * 70)
    
    for idx, producto in enumerate(productos, 1):
        stock = "Agotado" if producto.get("stock", 0) <= 0 else producto["stock"]
        print("{:<4} {:<30} ${:<11,.0f} {:<10} {:<10}".format(
            idx, producto["nombre"][:28], producto["precio"], producto["puntos"], stock))
    
    opcion = input("\nSeleccione el producto a comprar (0 para cancelar): ")
    opcion_num = validar_entero(opcion)
    
    if opcion_num is None:
        mostrar_mensaje("Debe ingresar un número válido", "error")
        return False
        
    if opcion_num == 0:
        return False
        
    if 1 <= opcion_num <= len(productos):
        producto = productos[opcion_num-1]
        
        if producto.get("stock", 0) <= 0:
            mostrar_mensaje("Este producto está agotado", "error")
            return False
            
        precio_final = aplicar_descuento(producto["precio"], usuario, usuarios)
        
        if precio_final != producto["precio"]:
            print(f"\nPrecio original: ${producto['precio']:,.0f}")
            print(f"Total a pagar: ${precio_final:,.0f}")
        else:
            print(f"\nTotal a pagar: ${precio_final:,.0f}")
        
        usuarios[usuario]["puntos"] += producto["puntos"]
        producto["stock"] -= 1
        
        mostrar_mensaje(
            f"\nHas ganado {producto['puntos']} puntos. Puntos totales: {usuarios[usuario]['puntos']}",
            "exito"
        )
        
        verificar_descuento(usuario, usuarios)
        return True
        
    mostrar_mensaje("Número de producto inválido", "error")
    return False