"""calculadora simple """

# entrada de datos
print("Bienvenido a la calculadora")
print("Seleccione una opción")

def mostrar_menu():
    print("\n--- Calculadora en Python ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numeros():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("Error: entrada no válida.")
        return None, None
     
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        elif opcion in ['1', '2', '3', '4']:
            a, b = obtener_numeros()
            if a is None or b is None:
                continue

            if opcion == '1':
                resultado = sumar(a, b)
            elif opcion == '2':
                resultado = restar(a, b)
            elif opcion == '3':
                resultado = multiplicar(a, b)
            elif opcion == '4':
                resultado = dividir(a, b)

            print("Resultado:", resultado)
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la calculadora
main()
