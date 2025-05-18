productos = [
    "Lay's", "Doritos", "Chochlitos", "Cheetos",
    "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
    "Gala", "Chocorramo", "Gansito", "Brownie",
    "Pepsi", "Manzana", "Colombiana", "Uva"
]

precios_pesos = [
    1000, 1500, 500, 900,
    500, 700, 600, 800,
    1000, 1800, 900, 2500,
    1500, 1500, 1500, 1500
]

cantidades = [
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 4
]

ventas = [0] * len(productos)
intercambios = []  # Registra productos reemplazados con ventas anteriores
ganancias = 0

TASA_DOLAR = 4000
moneda_actual = "COP"


def main():
    global moneda_actual
    while True:
        print("\n________ MENÚ PRINCIPAL ________")
        print("1. Retirar producto")
        print("2. Inventario")
        print("3. Informes")
        print("4. Configuración")
        print("5. Finalizar")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1': retirar_producto()
        elif opcion == '2': menu_inventario()
        elif opcion == '3': informes()
        elif opcion == '4': configuracion()
        elif opcion == '5': print("Fin del programa."); break
        else: print("Opción no válida.")


def mostrar_productos():
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos):
        fila, col = divmod(i, 4)
        precio = precios_pesos[i] if moneda_actual == "COP" else round(precios_pesos[i] / TASA_DOLAR, 2)
        unidad = moneda_actual if moneda_actual == "COP" else "USD"
        print(f"[{fila}{col}] {producto} - ${precio} {unidad} ({cantidades[i]} disponibles)")


def parse_codigo(msg):
    codigo = input(msg).strip()
    if len(codigo) != 2 or not codigo.isdigit():
        print("Código inválido. Use dos dígitos, p.ej. 01.")
        return None
    fila, col = int(codigo[0]), int(codigo[1])
    idx = fila * 4 + col
    if not (0 <= idx < len(productos)):
        print("Código fuera de rango.")
        return None
    return idx


def retirar_producto():
    global ganancias
    print("\n___________ RETIRAR PRODUCTO __________")
    mostrar_productos()
    while True:
        idx = parse_codigo("Código del producto (ej. 01): ")
        if idx is None: continue
        if cantidades[idx] == 0:
            print("Producto agotado.")
            return
        try:
            c = int(input(f"¿Cuántas unidades de '{productos[idx]}' desea?: ").strip())
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        if c < 1 or c > cantidades[idx]:
            print(f"Cantidad inválida, disponibles: {cantidades[idx]}.")
            continue
        cantidades[idx] -= c
        ganancias += precios_pesos[idx] * c
        ventas[idx] += c
        print(f"Retiradas {c} unidades de {productos[idx]}.")
        return


def menu_inventario():
    print("\nINVENTARIO")
    print("1. Añadir unidades")
    print("2. Reemplazar producto")
    print("3. Mostrar inventario")
    opc = input("Seleccione opción: ").strip()
    if opc == '1':
        mostrar_productos()
        idx = parse_codigo("Código del producto a recargar (ej. 02): ")
        if idx is None: return
        try:
            add = int(input(f"Unidades a agregar a '{productos[idx]}': ").strip())
        except ValueError:
            print("Número inválido."); return
        if add < 1 or cantidades[idx] + add > 5:
            print(f"Stock final debe estar entre 1 y 5.")
            return
        cantidades[idx] += add
        print(f"Nuevo stock de {productos[idx]}: {cantidades[idx]}.")

    elif opc == '2':
        mostrar_productos()
        idx = parse_codigo("Código del producto a reemplazar (ej. 10): ")
        if idx is None: return
        viejo = productos[idx]
        vtas = ventas[idx]
        if vtas > 0: intercambios.append((viejo, vtas))
        nombre = input("Nuevo nombre: ").strip()
        try:
            precio = int(input("Nuevo precio en COP: ").strip())
        except ValueError:
            print("Precio inválido."); return
        try:
            cant = int(input("Stock inicial (0-5): ").strip())
        except ValueError:
            print("Cantidad inválida."); return
        if cant < 0 or cant > 5:
            print("Stock debe ser 0-5."); return
        productos[idx], precios_pesos[idx], cantidades[idx], ventas[idx] = nombre, precio, cant, 0
        print(f"Reemplazado {viejo} -> {nombre}, stock {cant}.")

    elif opc == '3': mostrar_productos()
    else: print("Opción inválida.")


def informes():
    print("\nINFORMES")
    print(f"Ganancias: ${ganancias} COP / ${round(ganancias/TASA_DOLAR,2)} USD")
    print("\nVentas:")
    for i, p in enumerate(productos):
        if ventas[i]:
            tot = ventas[i]*precios_pesos[i]
            print(f"{p}: {ventas[i]} u - ${tot} COP / ${round(tot/TASA_DOLAR,2)} USD")
    if intercambios:
        print("\nProductos reemplazados con ventas previas:")
        for p, u in intercambios:
            print(f"{p}: {u} vendidas antes")


def configuracion():
    global moneda_actual
    print("\nCONFIGURACIÓN")
    print("1. Cambiar moneda","2. Restaurar",sep="\n")
    o = input("Opción: ")
    if o=='1': moneda_actual = "USD" if moneda_actual=="COP" else "COP"; print("Moneda:",moneda_actual)
    elif o=='2': restaurar_valores_fabrica()
    else: print("Inválida.")


def restaurar_valores_fabrica():
    global productos, precios_pesos, cantidades, ventas, intercambios, ganancias, moneda_actual
    productos = ["Lay's","Doritos","Chochlitos","Cheetos","Mani","Mani Moto",
                 "Mani con Pasas","Mani Mixto","Gala","Chocorramo","Gansito",
                 "Brownie","Pepsi","Manzana","Colombiana","Uva"]
    precios_pesos = [1000,1500,500,900,500,700,600,800,1000,1800,
                     900,2500,1500,1500,1500,1500]
    
    cantidades = [5]*15 + [4]
    ventas = [0]*len(productos)
    intercambios = []
    ganancias = 0
    moneda_actual = "COP"
    print("Restaurado valores de fábrica.")

if __name__ == "__main__": 
    main()
