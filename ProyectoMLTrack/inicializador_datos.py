from utils import guardar_datos

def cargar_datos_de_prueba():
    usuarios = [
        {"username": "juan", "password": "123", "rol": "comprador"},
        {"username": "maria", "password": "456", "rol": "vendedor"},
    ]

    productos = [
        {"id": "p1", "nombre": "Camisa", "precio": 25, "stock": 10, "vendedor": "maria"},
        {"id": "p2", "nombre": "Pantalón", "precio": 40, "stock": 5, "vendedor": "maria"},
    ]

    pedidos = [
    {"id": "ped1", "comprador": "juan", "id_producto": "p1", "cantidad": 2, "estado": "Pendiente"}
]

    guardar_datos("usuarios.json", usuarios)
    guardar_datos("productos.json", productos)
    guardar_datos("pedidos.json", pedidos)

if __name__ == "__main__":
    cargar_datos_de_prueba()
    print("Datos de prueba cargados correctamente.")