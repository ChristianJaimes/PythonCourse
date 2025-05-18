# comprador.py
from productos import obtener_productos_disponibles, obtener_producto_por_id
from pedidos import crear_pedido, listar_pedidos_por_comprador
from faq_bot import responder_pregunta

def menu_comprador(usuario_actual):
    while True:
        print("\n--- MENÚ COMPRADOR ---")
        print("1. Ver productos disponibles")
        print("2. Hacer pedido")
        print("3. Ver mis pedidos")
        print("4. Preguntas frecuentes (FAQ)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            productos = obtener_productos_disponibles()
            if productos:
                print("\nProductos disponibles:")
                for p in productos:
                    print(f"ID: {p['id']} - {p['nombre']} - Precio: ${p['precio']} - Stock: {p['stock']}")
            else:
                print("No hay productos disponibles.")
        
        elif opcion == "2":
            id_pedido = input("Ingrese ID para el nuevo pedido: ")
            id_producto = input("Ingrese ID del producto a comprar: ")
            cantidad = int(input("Cantidad: "))
            
            producto = obtener_producto_por_id(id_producto)
            if not producto:
                print("Producto no encontrado.")
                continue
            if producto["stock"] < cantidad:
                print("No hay suficiente stock.")
                continue

            nuevo_pedido = crear_pedido(id_pedido, usuario_actual, id_producto, cantidad)
            print(f"Pedido creado con éxito: {nuevo_pedido}")

        elif opcion == "3":
            pedidos = listar_pedidos_por_comprador(usuario_actual)
            if pedidos:
                print("\nTus pedidos:")
                for p in pedidos:
                    print(f"ID Pedido: {p['id']} - Producto: {p['id_producto']} - Cantidad: {p['cantidad']} - Estado: {p['estado']}")
            else:
                print("No tienes pedidos registrados.")

        elif opcion == "4":
            pregunta = input("Escribe tu pregunta: ")
            respuesta = responder_pregunta(pregunta)
            print("Respuesta:", respuesta)

        elif opcion == "5":
            print("Saliendo del menú comprador.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")