"""programa que simula una maquina expendedora de productos"""

productos = ["Lay's", "Doritos", "choclitos", "cheetoss", "mani", "mani moto","mani con pasas", "mani mixto","gala",
             "chocorramo","gansito","brwoni","pepsi","manzana","colombiana","uva"]
precios = [1000, 1500, 500, 900, 500, 700, 600, 800, 1000, 1800, 900, 2500, 1500, 1500, 1500, 1500]

cantidades = [5,5,5,5,
              5,5,5,5,
              5,5,5,5,
              5,5,5,4]

activos = [True] * len(productos) #estado inicial: todos activos

def mostrar_menu():
    #función que muestra el menú de la maquina expendedora
    
    print("------------ Bienvenido a la máquina expendedora ----------")
    print("Seleccione una opción:")
    print("1. comprar producto")
    print("2. inventario")
    print("3. informes")
    print("4. configuración")
    print("5. salir")
    
def comprar_producto():
    #función que permite comprar un producto
    
    print("productos disponibles:")
    for i, producto in enumerate(productos):
        fila = i // 4 #obtener fila
        columna = i % 4 #obtener columna
        codigo = f"{fila}{columna}" #codigo del producto
        print(f"[{codigo}]. {producto} - ${precios[i]}", end="\t")
        if columna == 3:
            print() #salto de linea cada 4 columns
            
    while True:
        try:
            codigo = (input("Seleccione el código del producto (5 para cancelar): "))
            
            if codigo == '5':
                print("Compra cancelada.")
                return
            
            if len(codigo) == 2 and codigo.isdigit():
                fila = int(codigo[0])
                columna = int(codigo[1])
                indice = fila * 4 + columna #pasar codigo a indice
            
                if 0 <= fila  <= 3 and 0 <= columna <= 3: #verificar validez del indice
                    indice = fila * 4 + columna
                    if not activos[indice]:
                        print("socket en mantenimiento, producto desactivado temporalmente")
                        return
                    if cantidades[indice] > 0:
                        cantidades[indice] -= 1
                        print(f"Has comprado un(a) {productos[indice]}. Gracias por tu compra!")
                        return
                    else:
                        print(f"Lo siento, {producto[indice]} no está disponible")
                else:
                    print("opcion inválida, intente nuevamente")
            else:
                print("codigo no valido. Intente de nuevo")
        except ValueError:
            print("por favor, ingrese un número válido")
        
def inventario():
    #función que muestra el inventario de la maquina expendedora
    print("Inventario:")
    i = 0 #indice
    for producto in productos:
        print(f"{producto} - Cantidad: {cantidades[i]}")
        i += 1 #incrementar el indice

def modificar_inventario():
    #función que permite cambiar las cantidades de los productos
    print("Modificar inventario:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto} - Cantidad actual: {cantidades[i]}")

    try:
        opcion = int(input("Seleccione el número del producto que desea modificar (0 para cancelar): "))
        if opcion == 0:
            print("Modificación cancelada.")
            return
        if 1 <= opcion <= len(productos):
            indice = opcion - 1
            while True:
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {productos[indice]} (máximo 5): "))
                    if 0 <= nueva_cantidad <= 5:
                        cantidades[indice] = nueva_cantidad
                        print(f"Cantidad de {productos[indice]} actualizada a {nueva_cantidad}.")
                        return
                    else:
                        print("La cantidad debe estar entre 0 y 5.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        else:
            print("Producto fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
                
def agregar_productos():
    #función que permite agregar productos al inventario
    print("Agregar productos:")
    while True:
        producto = input("Ingrese el nombre del nuevo producto (0 para cancelar): ")
        if producto == '0':
            print("Agregando productos cancelado.")
            return
        try:
            precio = float(input(f"Ingrese el precio para {producto}: "))
            cantidad = int(input(f"Ingrese la cantidad para {producto} (maximo 5): "))
            
            if cantidad < 0 or cantidad > 5:
                print("La cantidad debe estar entre 0 y 5.")
                continue
            
            productos.append(producto)
            precios.append(precio)
            cantidades.append(cantidad)
            activos = [True] #agregar el nuevo producto como activo
            print(f"Producto {producto} agregado con éxito.")
        except ValueError:
            print("Por favor, ingrese valores válidos.")
            
def eliminar_productos():
    #función que permite eliminar productos del inventario
    print("Eliminar productos:")
    while True:
        producto = input("Ingrese el nombre del producto a eliminar (0 para cancelar): ")
        if producto == '0':
            print("Eliminando productos cancelado.")
            return
        if producto in productos:
            index = productos.index(producto)
            productos.pop(index)
            precios.pop(index)
            cantidades.pop(index)
            print(f"Producto {producto} eliminado con éxito.")
        else:
            print(f"Producto {producto} no encontrado en el inventario.")
            
def funciones_inventario():
    #función con las opciones del inventario
    #mostrar submenú inventario
    print("------------ Submenú Inventario ----------")
    print("Seleccione una opción:")
    print("1. mostrar inventario actual")
    print("2. modificar inventario")
    print("3. agregar productos")
    print("4. eliminar productos")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Inventario cancelado.")
                return
            elif opcion == 1:
                inventario()
            elif opcion == 2:
                modificar_inventario()
            elif opcion == 3:
                agregar_productos()
            elif opcion == 4:
                eliminar_productos()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
def informe_ganancias():
    #función que muestra los informes de ganancias
    print("Informe de ganancias:")
    total_ganancias = sum(precios[i] * (cantidades[i] - cantidades[i]) for i in range(len(productos)))
    print(f"Total de ganancias: ${total_ganancias}")
    
def informe_ventas():
    #función que muestra los informes de ventas
    print("Informe de ventas:")
    total_ventas = sum(precios[i] * (cantidades[i] - cantidades[i]) for i in range(len(productos)))
    print(f"Total de ventas: ${total_ventas}")
    
def funciones_informes():
    #funcion con las opciones de informes
    print("------------ Submenú Informes ----------")
    print("Seleccione una opción:")
    print("1. mostrar informes de ganancias")
    print("2. mostrar informes de ventas")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Informes cancelado.")
                return
            elif opcion == 1:
                print("Mostrando informes de ganancias...")
                informe_ganancias()
            elif opcion == 2:
                print("Mostrando informes de ventas...")
                informe_ventas()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.") 

def restaurar_fabricar():
    #función que restaura los valores de fábrica
    global productos, precios, cantidades
    
    productos = ["Lay's", "Doritos", "choclitos", "cheetoss", "mani", "mani moto","mani con pasas", "mani mixto","gala",
                 "chocorramo","gansito","brwoni","pepsi","manzana","colombiana","uva"]
    precios = [1000, 1500, 500, 900, 500, 700, 600, 800, 1000, 1800, 900, 2500, 1500, 1500, 1500, 1500]
    cantidades = [5,5,5,5,
                    5,5,5,5,
                    5,5,5,5,
                    5,5,5,4]
    print("Valores restaurados a los valores de fábrica.")

def desactivar_producto():
    #función que desactiva un producto temporalmente por reparación u otra razón
    print("Activar/Desactivar productos:")
    for i, producto in enumerate(productos):
        estado = "Activo" if activos[i] else "Inactivo"
        print(f"{i + 1}. {producto} - Estado: {estado}")
    try:
        opcion = int(input("Ingrese el número del producto a cambiar estado (0 para cancelar): "))
        if opcion == 0:
            return
        if 1 <= opcion <= len(productos):
            indice = opcion - 1
            activos[indice] = not activos[indice]
            nuevo_estado = "Activo" if activos[indice] else "Inactivo"
            print(f"{productos[indice]} ahora está: {nuevo_estado}")
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Entrada no válida.")
    
def configuracion():
    #función que permite cambiar la configuración de la máquina expendedora
    print("------------ Submenú Configuración ----------")
    print("Seleccione una opción:")
    print("1. restaurar valores de fábrica")
    print("0. volver al menú principal")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (0 para cancelar): "))
            if opcion == 0:
                print("Configuración cancelada.")
                return
            elif opcion == 1:
                restaurar_fabricar()
            elif opcion == 2:
                desactivar_producto()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")                   
            
def main():
    #función principal que ejecuta el programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0 para salir): ")
        
        if opcion == '5':
            print("¡Gracias por usar la máquina expendedora!")
            break
        elif opcion == '1':
            comprar_producto()
        elif opcion == '2':
            funciones_inventario()
        elif opcion == '3':
            funciones_informes()
        elif opcion == '4':
            configuracion()
        else:
            print("Opción no válida. Intente nuevamente.")
            
if __name__ == "__main__":
    main()
# Ejecutar el programa
# main()
