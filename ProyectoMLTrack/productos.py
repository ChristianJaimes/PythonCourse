from utils import cargar_productos, guardar_productos

def obtener_productos_disponibles():
    productos = cargar_productos()
    return [p for p in productos if p["stock"] > 0]

def obtener_producto_por_id(id_producto):
    productos = cargar_productos()
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None

def obtener_productos_por_vendedor(nombre_vendedor):
    productos = cargar_productos()
    return [p for p in productos if p["vendedor"] == nombre_vendedor]

def agregar_producto(producto):
    productos = cargar_productos()
    productos.append(producto)
    guardar_productos(productos)

def actualizar_stock(id_producto, cantidad):
    productos = cargar_productos()
    for producto in productos:
        if producto["id"] == id_producto:
            producto["stock"] -= cantidad
            if producto["stock"] < 0:
                producto["stock"] = 0
            guardar_productos(productos)
            return True
    return False
