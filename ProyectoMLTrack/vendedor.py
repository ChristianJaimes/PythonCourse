# vendedor.py
from productos import obtener_productos_por_vendedor, agregar_producto
from pedidos import listar_pedidos_por_vendedor, actualizar_estado_pedido

def menu_vendedor(usuario_actual):
    while True:
        print("\n--- MENÚ VENDEDOR ---")
        print("1. Ver mis productos")
        print("2. Agregar nuevo producto")
        print("3. Ver pedidos de mis productos")
        print("4. Cambiar estado de pedido")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            productos = obtener_productos_por_vendedor(usuario_actual)
            if productos:
                print("\nTus productos:")
                for p in productos:
                    print(f"ID: {p['id']} - {p['nombre']} - Precio: ${p['precio']} - Stock: {p['stock']}")
            else:
                print("No tienes productos registrados.")

        elif opcion == "2":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            nuevo_producto = {
                "id": id_producto,
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "vendedor": usuario_actual
            }
            agregar_producto(nuevo_producto)
            print("Producto agregado con éxito.")

        elif opcion == "3":
            productos = obtener_productos_por_vendedor(usuario_actual)
            pedidos = listar_pedidos_por_vendedor(usuario_actual, productos)
            if pedidos:
                print("\nPedidos de tus productos:")
                for p in pedidos:
                    print(f"ID Pedido: {p['id']} - Producto: {p['id_producto']} - Cantidad: {p['cantidad']} - Estado: {p['estado']}")
            else:
                print("No hay pedidos para tus productos.")

        elif opcion == "4":
            id_pedido = input("Ingrese ID del pedido a actualizar: ")
            nuevo_estado = input("Nuevo estado (Pendiente, Enviado, Entregado, Cancelado): ")
            if actualizar_estado_pedido(id_pedido, nuevo_estado):
                print("Estado actualizado.")
            else:
                print("Pedido no encontrado.")

        elif opcion == "5":
            print("Saliendo del menú vendedor.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")