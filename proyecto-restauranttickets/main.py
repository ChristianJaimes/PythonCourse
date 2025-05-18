from datetime import date, datetime
from zoneinfo import ZoneInfo

# Configuración de descuento
DESCUENTO = {
    "activo": True,
    "tope_minimo": 100000.0,
    "porcentaje": 0.10  # 10%
}

# Definición de combos
COMBOS = {
    1: {"nombre": "Combo de Tacos al Pastor", "precio": 42000.0, "tiempo": 15},
    2: {"nombre": "Combo de Tacos de Birria", "precio": 42000.0, "tiempo": 20},
    3: {"nombre": "Combo de Quesadillas",      "precio": 35000.0, "tiempo": 10},
}

# Almacenamiento en memoria
pedidos = {}
fila = []
estadisticas = {
    "fecha": date.today().isoformat(),
    "total_pedidos": 0,
    "recaudado": 0.0,
    "ventas_por_combo": {cid: 0 for cid in COMBOS}
}

# Contador global de pedidos
_id_counter = 0

def generar_id():
    global _id_counter
    _id_counter += 1
    return _id_counter

def calcular_descuento(subtotal: float) -> float:
    if DESCUENTO["activo"] and subtotal >= DESCUENTO["tope_minimo"]:
        return subtotal * DESCUENTO["porcentaje"]
    return 0.0

def reiniciar_datos():
    global estadisticas, _id_counter
    pedidos.clear()
    fila.clear()
    _id_counter = 0
    estadisticas = {
        "fecha": date.today().isoformat(),
        "total_pedidos": 0,
        "recaudado": 0.0,
        "ventas_por_combo": {cid: 0 for cid in COMBOS}
    }
    print("\nDatos reiniciados correctamente.")

def listar_combos():
    print("\n==================== COMBOS DISPONIBLES ====================")
    print(f"{'ID':<4}{'Nombre':<30}{'Precio':<12}{'Tiempo(min)'}")
    print('-' * 60)
    for cid, info in COMBOS.items():
        nombre = info['nombre']
        precio = f"{info['precio']:.2f}"
        tiempo = f"{info['tiempo']}"
        print(f"{cid:<4}{nombre:<30}{precio:<12}{tiempo}")
    print()

def leer_entrada(prompt: str, minimo: int = None, maximo: int = None) -> int | str:
    while True:
        entrada = input(prompt).strip()
        if entrada.lower() == 'c':
            return 'cancelar'
        if entrada.lower() == 'f':
            return 'finalizar'
        try:
            valor = int(entrada)
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número entero o una opción válida (f/c).")

def registrar_pedido():
    combos_en_pedido = []
    subtotal = 0.0
    tiempo_total = 0
    print("\nIngrese los combos del pedido. Escriba 'f' para finalizar o 'c' para cancelar y volver al menú principal.")

    while True:
        listar_combos()
        respuesta = leer_entrada("Seleccione el ID del combo ('f' para finalizar, 'c' para cancelar): ", minimo=1, maximo=len(COMBOS))
        if respuesta == 'cancelar':
            print("Pedido cancelado. Regresando al menú principal.")
            return
        if respuesta == 'finalizar':
            if not combos_en_pedido:
                print("No se puede registrar un pedido vacío.")
                continue
            break
        cid = respuesta
        cantidad = leer_entrada("Cantidad de unidades: ", minimo=1)
        if cantidad == 'cancelar':
            print("Pedido cancelado. Regresando al menú principal.")
            return
        combo = COMBOS[cid]
        total_combo = combo['precio'] * cantidad
        subtotal += total_combo
        tiempo_total += combo['tiempo'] * cantidad
        combos_en_pedido.append((cid, cantidad))

    desc = calcular_descuento(subtotal)
    total = subtotal - desc
    marca_tiempo = datetime.now(ZoneInfo("America/Bogota")).strftime("%Y-%m-%d %H:%M:%S")
    pid = generar_id()

    # Guardar pedido
    pedido = {
        'id_pedido': pid,
        'combos': combos_en_pedido,
        'subtotal': subtotal,
        'descuento': desc,
        'total': total,
        'tiempo_estimado': tiempo_total,
        'estado': 'en cola',
        'marca_tiempo': marca_tiempo
    }
    pedidos[pid] = pedido
    fila.append(pid)

    for cid, cantidad in combos_en_pedido:
        actualizar_estadisticas(cid, cantidad, 0.0)

    estadisticas['recaudado'] += total
    estadisticas['total_pedidos'] += 1

    # Ticket de pedido
    print("\n========== TICKET DE PEDIDO ==========")
    print(f"ID Pedido : {pid}")
    print(f"Fecha/Hora : {marca_tiempo}")
    print("-" * 38)
    for cid, cantidad in combos_en_pedido:
        nombre = COMBOS[cid]['nombre']
        precio_unitario = COMBOS[cid]['precio']
        total_linea = precio_unitario * cantidad
        print(f"{nombre:<30}")
        print(f"  {cantidad} x {precio_unitario:.2f} = {total_linea:.2f}")
    print("-" * 38)
    print(f"Subtotal   : {subtotal:.2f} COP$")
    print(f"Descuento  : {desc:.2f} COP$")
    print(f"Total      : {total:.2f} COP$")
    print(f"Tiempo est : {tiempo_total} min")
    print('=' * 38)

def actualizar_estadisticas(cid: int, cantidad: int, total: float):
    hoy = date.today().isoformat()
    if estadisticas['fecha'] != hoy:
        reiniciar_datos()
    estadisticas['ventas_por_combo'][cid] += cantidad

def ver_fila():
    if not fila:
        print("\nLa fila está vacía.")
        return
    print("\n====== FILA DE PEDIDOS ======")
    print(f"{'ID':<6}{'Tiempo restante (min)'}")
    print('-' * 29)
    acumulado = 0
    for pid in fila:
        p = pedidos[pid]
        acumulado += p['tiempo_estimado']
        print(f"{pid:<6}{acumulado}")
    print('-' * 29)
    print(f"Tiempo total: {acumulado} min")
    print('=' * 29)

def ver_estadisticas():
    if estadisticas['total_pedidos'] == 0:
        print("\nNo hay estadísticas para mostrar.")
        return
    print("\n=========== ESTADÍSTICAS DEL DÍA ===========")
    print(f"Fecha           : {estadisticas['fecha']}")
    print(f"Total pedidos   : {estadisticas['total_pedidos']}")
    print(f"Total recaudado : {estadisticas['recaudado']:.2f} COP$")
    print('-' * 44)
    print(f"{'ID':<4}{'Combo':<30}{'Vendidos'}")
    print('-' * 44)
    for cid, qty in estadisticas['ventas_por_combo'].items():
        nombre = COMBOS[cid]['nombre']
        print(f"{cid:<4}{nombre:<30}{qty}")
    print('=' * 44)

def mostrar_menu() -> int:
    print("\n=========== MENÚ ===========")
    print("1. Generar pedido")
    print("2. Ver fila")
    print("3. Ver estadísticas diarias")
    print("4. Reiniciar datos")
    print("5. Salir")
    print("=" * 28)
    return leer_entrada("\nSeleccione una opción (1-5): ", minimo=1, maximo=5)

def main():
    print("\n¡Bienvenido a la app!")
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            ver_fila()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reiniciar_datos()
        else:
            print("\nGracias por usar la aplicación. ¡Hasta luego!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. Saliendo.\n")
    except Exception as e:
        print(f"\nError inesperado: {e}")
