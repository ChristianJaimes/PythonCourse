from datetime import datetime

# Datos iniciales
usuarios = []

productos = [
    {"id": 1, "nombre": "Masa para croissants", "unidad": "kg"},
    {"id": 2, "nombre": "Glaseado de vainilla", "unidad": "litro"},
    {"id": 3, "nombre": "Crema pastelera", "unidad": "kg"},
    {"id": 4, "nombre": "Relleno de manzana", "unidad": "kg"},
    {"id": 5, "nombre": "Base de pizza congelada", "unidad": "unidad"}
]

lotes = []
solicitudes = []

# Menú principal
def mostrar_menu():
    print("Menú de Gestión de Compras - Rich's")
    print("1. Agregar usuario")
    print("2. Ver productos")
    print("3. Registrar lote de producto")
    print("4. Crear solicitud de compra")
    print("5. Ver solicitudes")
    print("6. Aprobar o rechazar solicitudes")
    print("7. Ver inventario")
    print("8. Ver historial general")
    print("0. Salir")

# Función para agregar un nuevo usuario
def agregar_usuario():
    nombre = input("Nombre del usuario: ")
    usuarios.append({"id": len(usuarios) + 1, "nombre": nombre})
    print("Usuario agregado.")

# Función para mostrar la lista de productos
def ver_productos():
    print("Productos disponibles:")
    for producto in productos:
        print(f"{producto['id']}. {producto['nombre']} ({producto['unidad']})")

# Función para registrar un nuevo lote
def registrar_lote():
    ver_productos()
    try:
        producto_id = int(input("ID del producto: "))
        cantidad = float(input("Cantidad: "))
        numero_lote = input("Número de lote: ")
        fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        lotes.append({
            "id": len(lotes) + 1,
            "producto_id": producto_id,
            "cantidad": cantidad,
            "numero_lote": numero_lote,
            "vencimiento": fecha_vencimiento
        })
        print("Lote registrado.")
    except:
        print("Error en los datos. Intenta de nuevo.")

# Función para crear una nueva solicitud de compra
def crear_solicitud():
    if not usuarios:
        print("Agrega usuarios primero.")
        return

    print("Usuarios disponibles:")
    for usuario in usuarios:
        print(f"{usuario['id']}. {usuario['nombre']}")

    try:
        usuario_id = int(input("ID del usuario solicitante: "))
        productos_solicitados = []

        while True:
            ver_productos()
            producto_id = int(input("ID del producto a solicitar (0 para terminar): "))
            if producto_id == 0:
                break
            cantidad = float(input("Cantidad: "))
            productos_solicitados.append({"producto_id": producto_id, "cantidad": cantidad})

        solicitud = {
            "id": len(solicitudes) + 1,
            "usuario_id": usuario_id,
            "estado": "pendiente",
            "productos": productos_solicitados
        }

        solicitudes.append(solicitud)
        print("Solicitud registrada.")
    except:
        print("Error al registrar solicitud.")

# Función para mostrar todas las solicitudes
def ver_solicitudes():
    print("Solicitudes registradas:")
    for solicitud in solicitudes:
        usuario = next((usuario for usuario in usuarios if usuario["id"] == solicitud["usuario_id"]), {"nombre": "Desconocido"})
        print(f"Solicitud ID: {solicitud['id']} | Usuario: {usuario['nombre']} | Estado: {solicitud['estado']}")
        for item in solicitud["productos"]:
            producto = next((producto for producto in productos if producto["id"] == item["producto_id"]), {})
            print(f"{producto.get('nombre', 'Desconocido')}: {item['cantidad']} {producto.get('unidad', '')}")

# Función para aprobar o rechazar una solicitud
def aprobar_rechazar():
    ver_solicitudes()
    try:
        id_solicitud = int(input("ID de la solicitud a revisar: "))
        solicitud = next((solicitud for solicitud in solicitudes if solicitud["id"] == id_solicitud), None)

        if solicitud:
            print("1. Aprobar")
            print("2. Rechazar")
            opcion = input("Opción: ")

            if opcion == "1":
                solicitud["estado"] = "aprobada"
                print("Solicitud aprobada.")
            elif opcion == "2":
                solicitud["estado"] = "rechazada"
                print("Solicitud rechazada.")
            else:
                print("Opción no válida.")
        else:
            print("Solicitud no encontrada.")
    except:
        print("Error en la entrada.")

# Función para ver el inventario actual
def ver_inventario():
    print("Inventario actual por lote:")
    for lote in lotes:
        producto = next((producto for producto in productos if producto["id"] == lote["producto_id"]), {})
        print(f"{producto.get('nombre', 'Desconocido')} | {lote['cantidad']} {producto.get('unidad', '')} | "
              f"Lote: {lote['numero_lote']} | Vence: {lote['vencimiento']}")

# Función para ver un resumen del historial
def ver_historial():
    print("Historial del sistema:")
    print(f"- Usuarios registrados: {len(usuarios)}")
    print(f"- Productos en catálogo: {len(productos)}")
    print(f"- Lotes registrados: {len(lotes)}")
    print(f"- Solicitudes realizadas: {len(solicitudes)}")

# Bucle principal del sistema
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_usuario()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        registrar_lote()
    elif opcion == "4":
        crear_solicitud()
    elif opcion == "5":
        ver_solicitudes()
    elif opcion == "6":
        aprobar_rechazar()
    elif opcion == "7":
        ver_inventario()
    elif opcion == "8":
        ver_historial()
    elif opcion == "0":
        print("Saliendo del sistema. ¡Gracias!")
        break
    else:
        print("Opción no válida.")
