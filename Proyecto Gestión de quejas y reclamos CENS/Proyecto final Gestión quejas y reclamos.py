# Estructuras de datos
usuarios = {}
# Diccionario de reclamos
# Clave: ID del reclamo (int)
# Valor: Diccionario con:
#   - usuario_id: str → ID del usuario que lo radicó
#   - tipo: str → Tipo de reclamo ("Falla de energía", etc.)
#   - descripcion: str → Detalles del reclamo
#   - adjuntos: list[str] → Archivos adjuntos (simulados)
#   - estado: str → Estado actual ("Abierto", "En proceso", "Finalizado")y
#   - ubicacion: str → Ubicación geográfica en formato "lat,long"
#   - solucion: str or None → Respuesta del asesor (solo si está finalizado)

reclamos = {}
# Diccionario de feedbacks
# Clave: ID del feedback (int)
# Valor: Diccionario con:
#   - usuario_id: str → ID del cliente que envió el comentario
#   - comentario: str → Opinión sobre el servicio

feedbacks = {}
# Lista de notificaciones
# Cada notificación es una tupla:
#   (correo_destinatario: str, mensaje: str)

notificaciones = []
# Lista de mensajes de chat
# Cada mensaje es una tupla:
#   (usuario_id: str, mensaje: str)

mensajes_chat = []
# Cuenta predeterminada del asesor

usuarios["isa"] = {
    "nombre": "Administrador",
    "correo": "admin@cens.com",
    "rol": "asesor",
    "password": "isa123",
    "reclamos": [],
    "feedbacks": []
}

def registrar_usuario():
    usuario_id = input("Ingrese su ID de usuario: ")
    if usuario_id in usuarios:
        print("Este ID ya está registrado.")
        return None
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    usuarios[usuario_id] = {
        "nombre": nombre,
        "correo": correo,
        "rol": "cliente",
        "reclamos": [],
        "feedbacks": []
    }
    print(f"Cliente {nombre} registrado con éxito.")
    return usuario_id

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    print("1. Ingresar como Cliente")
    print("2. Ingresar como Asesor")
    tipo = input("Seleccione el tipo de usuario: ")

    if tipo == "1":
        usuario_id = input("Ingrese su ID de usuario: ")
        if usuario_id in usuarios and usuarios[usuario_id]["rol"] == "cliente":
            print(f"Bienvenido/a {usuarios[usuario_id]['nombre']}!")
            return usuario_id, "cliente"
        else:
            print("Usuario no encontrado o no es cliente.")
            return None, None

    elif tipo == "2":
        usuario_id = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if usuario_id in usuarios and usuarios[usuario_id]["rol"] == "asesor" and usuarios[usuario_id]["password"] == contraseña:
            print("Sesión iniciada como Asesor.")
            return usuario_id, "asesor"
        else:
            print("Credenciales incorrectas.")
            return None, None
    else:
        print("Opción inválida.")
        return None, None

def radicar_reclamo(usuario_id):
    print("\nTipos de reclamos:")
    tipos = ["Falla de energía", "Medidor dañado", "Cobro incorrecto", "Poda de árboles", "Otro"]
    for i, tipo in enumerate(tipos, 1):
        print(f"{i}. {tipo}")
    opcion = int(input("Seleccione el número del tipo de reclamo: "))
    tipo_reclamo = tipos[opcion - 1]
    descripcion = input("Describa su reclamo: ")
    adjunto = input("Ingrese nombre de archivo adjunto (simulado): ")
    ubicacion = input("Ingrese ubicación del problema (lat,long): ")

    reclamo_id = len(reclamos) + 1
    reclamos[reclamo_id] = {
        "usuario_id": usuario_id,
        "tipo": tipo_reclamo,
        "descripcion": descripcion,
        "adjuntos": [adjunto],
        "estado": "Abierto",
        "ubicacion": ubicacion,
        "solucion": None
    }
    usuarios[usuario_id]["reclamos"].append(reclamo_id)
    print(f"Reclamo #{reclamo_id} registrado. Estado: Abierto.")
    return reclamo_id

def seguimiento_reclamos_cliente(usuario_id):
    ids = usuarios[usuario_id]["reclamos"]
    if not ids:
        print("No hay reclamos para este usuario.")
        return
    for rid in ids:
        r = reclamos[rid]
        print(f"Reclamo #{rid} - {r['tipo']}: Estado: {r['estado']} | Solución: {r['solucion'] or 'Pendiente'}")

def gestionar_reclamos_asesor():
    pendientes = [rid for rid, r in reclamos.items() if r["estado"] != "Finalizado"]
    if not pendientes:
        print("No hay reclamos pendientes.")
        return
    for rid in pendientes:
        r = reclamos[rid]
        print(f"\nReclamo #{rid} - {r['tipo']} (Usuario {r['usuario_id']})")
        print(f"Descripción: {r['descripcion']}")
        print(f"Estado actual: {r['estado']}")
        print("¿Qué acción desea tomar?")
        if r['estado'] == "Abierto":
            print("1. Marcar como En proceso")
            print("2. Omitir")
            op = input("Seleccione una opción: ")
            if op == "1":
                reclamos[rid]["estado"] = "En proceso"
                enviar_notificacion(r["usuario_id"], f"Su reclamo #{rid} está siendo atendido (En proceso).")
                print(f"Reclamo #{rid} actualizado a estado: En proceso.")
            elif op == "2":
                continue
            else:
                print("Opción no válida.")
        elif r['estado'] == "En proceso":
            print("1. Finalizar y agregar respuesta")
            print("2. Omitir")
            op = input("Seleccione una opción: ")
            if op == "1":
                solucion = input("Ingrese la solución o respuesta al reclamo: ")
                reclamos[rid]["estado"] = "Finalizado"
                reclamos[rid]["solucion"] = solucion
                enviar_notificacion(r["usuario_id"], f"Su reclamo #{rid} ha sido resuelto.\nSolución: {solucion}")
                print(f"Reclamo #{rid} marcado como FINALIZADO.")
            elif op == "2":
                continue
            else:
                print("Opción no válida.")
    print("Gestión de reclamos completada.")

def enviar_notificacion(usuario_id, mensaje):
    correo = usuarios[usuario_id]['correo']
    notificaciones.append((correo, mensaje))
    print(f"Notificación enviada a {correo}: {mensaje}")

def chat_cliente(usuario_id):
    mensaje = input("Escriba su mensaje para atención al cliente: ")
    mensajes_chat.append((usuario_id, mensaje))
    print("Mensaje enviado. El asesor responderá pronto.")

def responder_chat_asesor():
    if not mensajes_chat:
        print("No hay mensajes de clientes.")
        return
    for usuario_id, mensaje in mensajes_chat:
        respuesta = "Gracias por su mensaje. Hemos recibido su solicitud y la estamos procesando."
        print(f"\nChat de {usuario_id}: {mensaje}")
        print(f"Asesor responde: {respuesta}")
        enviar_notificacion(usuario_id, "Respuesta del asesor: " + respuesta)
    mensajes_chat.clear()

def registrar_feedback(usuario_id):
    comentario = input("¿Qué opina del servicio recibido?: ")
    fid = len(feedbacks) + 1
    feedbacks[fid] = {
        "usuario_id": usuario_id,
        "comentario": comentario
    }
    usuarios[usuario_id]["feedbacks"].append(comentario)
    print("¡Gracias por su retroalimentación!")

def ver_feedbacks_asesor():
    if not feedbacks:
        print("No hay feedbacks registrados.")
        return
    print("\n--- Comentarios de los clientes ---")
    for fid, fb in feedbacks.items():
        print(f"Usuario {fb['usuario_id']}: {fb['comentario']}")

# Menú Principal
print("Bienvenido a la aplicación CENS.")

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrarse como cliente")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()

    elif opcion == "2":
        usuario_id, rol = iniciar_sesion()
        if usuario_id and rol == "cliente":
            while True:
                print("\n--- Menú Cliente ---")
                print("1. Radicar reclamo")
                print("2. Ver seguimiento de reclamos")
                print("3. Chatear con atención")
                print("4. Dejar feedback")
                print("5. Cerrar sesión")
                op = input("Seleccione una opción: ")
                if op == "1":
                    radicar_reclamo(usuario_id)
                elif op == "2":
                    seguimiento_reclamos_cliente(usuario_id)
                elif op == "3":
                    chat_cliente(usuario_id)
                elif op == "4":
                    registrar_feedback(usuario_id)
                elif op == "5":
                    break
                else:
                    print("Opción no válida.")

        elif usuario_id and rol == "asesor":
            while True:
                print("\n--- Menú Asesor ---")
                print("1. Ver y gestionar reclamos")
                print("2. Responder chats de clientes")
                print("3. Ver feedbacks de clientes")
                print("4. Cerrar sesión")
                op = input("Seleccione una opción: ")
                if op == "1":
                    gestionar_reclamos_asesor()
                elif op == "2":
                    responder_chat_asesor()
                elif op == "3":
                    ver_feedbacks_asesor()
                elif op == "4":
                    break
                else:
                    print("Opción no válida.")

    elif opcion == "3":
        print("Gracias por usar la aplicación CENS. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
