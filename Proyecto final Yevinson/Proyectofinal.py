print("Bienvenidos a la plataforma de la agencia publica de empleo sena! ")
usuarios = {}

def registrar_aspirante(nombre):
    contraseña = input("Cree una contraseña: ")
    historial_laboral = input("Ingrese su historial laboral: ")
    historial_academico = input("Ingrese su historial académico: ")
    contacto_aspirante = input("Ingrese información de contacto: ")
    
    usuarios[nombre] = {
        "rol": "aspirante",
        "contraseña": contraseña,
        "historial_laboral": historial_laboral,
        "historial_academico": historial_academico,
        "contacto_aspirante": contacto_aspirante
    }
    print("Registro exitoso.")

def eliminar_aspirante(nombre):
    confirmacion = input(f"¿Estás seguro de que deseas eliminar el usuario '{nombre}'? (s/n): ").lower()
    if confirmacion == 's':
        del usuarios[nombre]
        print("Usuario eliminado exitosamente.")
    else:
        print("Operación cancelada.")

def menu_principal():
    while True:
        print("plataforma agencia publica de empleo")
        print("1. Ingresar como Aspirante")
        print("2. Ingresar como Empleador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_aspirante()
        elif opcion == "2":
            menu_empleador()
        elif opcion == "3":
            print("Gracias por usar la plataforma.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_aspirante():
    print("\n--- Menú Aspirante ---")
    nombre = input("Ingrese su nombre de usuario: ")

    if nombre not in usuarios:
        print("Nuevo usuario detectado. Registre su información.")
        registrar_aspirante(nombre)
    else:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[nombre]["contraseña"] != contraseña:
            print("Contraseña incorrecta.")
            return

        while True:
            print(f"\nBienvenido de nuevo, {nombre}")
            print("1. Actualizar información")
            print("2. Eliminar cuenta")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                 actualizar_aspirante(nombre)

            elif opcion == "2":
                confirmacion = input("¿Está seguro que desea eliminar su cuenta? (s/n): ").lower()
                if confirmacion == "s":
                    eliminar_aspirante(nombre)
                    break
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        

def actualizar_aspirante(nombre):
    print("\n--- Actualización de Datos ---")
    historial_laboral = input("Actualizar historial laboral: ")
    historial_academico = input("Actualizar historial académico: ")
    contacto_aspirante = input("actualizar contacto aspirante:")
    contraseña = input("actualizar contraseña:")
    usuarios[nombre]["historial_laboral"] = historial_laboral
    usuarios[nombre]["historial_academico"] = historial_academico
    usuarios[nombre]["contacto_aspirante"] = contacto_aspirante
    print("Datos actualizados exitosamente.")

def menu_empleador():
    print("\n--- Menú Empleador ---")
    print("Lista de aspirantes registrados:")
    aspirantes = [nombre for nombre, datos in usuarios.items() if datos["rol"] == "aspirante"]

    if not aspirantes:
        print("No hay aspirantes registrados aún.")
        return

    for i, aspirante in enumerate(aspirantes, 1):
        print(f"{i}. {aspirante}")

    opcion = input("Seleccione el número del aspirante para ver su información (o presione Enter para volver): ")
    if opcion.isdigit():
        index = int(opcion) - 1
        if 0 <= index < len(aspirantes):
            nombre = aspirantes[index]
            datos = usuarios[nombre]
            print(f"\n--- Información de {nombre} ---")
            print("Historial Laboral:", datos["historial_laboral"])
            print("Historial Académico:", datos["historial_academico"])
            print("contacto aspirante:", datos["contacto_aspirante"])
        else:
            print("Selección inválida.")
    else:
        print("Regresando al menú principal...")

menu_principal()
