from utils import cargar_pedidos, guardar_pedidos
from productos import actualizar_stock

def crear_pedido(id_pedido, comprador, id_producto, cantidad):
    pedidos = cargar_pedidos()
    nuevo_pedido = {
        "id": id_pedido,
        "comprador": comprador,
        "id_producto": id_producto,
        "cantidad": cantidad,
        "estado": "Pendiente"
    }
    pedidos.append(nuevo_pedido)
    guardar_pedidos(pedidos)
    actualizar_stock(id_producto, cantidad)
    return nuevo_pedido

def listar_pedidos_por_comprador(nombre_comprador):
    pedidos = cargar_pedidos()
    return [p for p in pedidos if p["comprador"] == nombre_comprador]

def listar_pedidos_por_vendedor(nombre_vendedor, productos_vendedor):
    pedidos = cargar_pedidos()
    ids_productos = [p["id"] for p in productos_vendedor]
    return [pedido for pedido in pedidos if pedido["id_producto"] in ids_productos]

def actualizar_estado_pedido(id_pedido, nuevo_estado):
    pedidos = cargar_pedidos()
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            pedido["estado"] = nuevo_estado
            guardar_pedidos(pedidos)
            return True
    return False