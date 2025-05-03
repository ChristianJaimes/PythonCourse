def suma(x, y):
    r = x + y
    print(f"El resultado de la suma es {r}")

def resta(x, y):
    r = x - y
    print(f"El resultado de la resta es {r}")

def multiplicacion(x, y):
    r = x * y
    print(f"El resultado de la multiplicación es {r}")

def division(x, y):
    if y != 0:
        r = x / y
        print(f"El resultado de la división es {r}")
    else:
        print("No se puede dividir entre cero.")

def obtener_valores():
    numero1 = float(input("Ingresa un número: "))
    numero2 = float(input("Ingresa otro número: "))
    return numero1, numero2

if __name__ == '__main__':
    print("Calculadora")

    while True:
        opciones = """
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
        """
        print(opciones)
        opcion = input("Ingresa el número de la opción que quieres operar: ")

        if opcion == "5":
            print("¡Chao! Gracias por usar la calculadora.")
            break  # Sale del bucle y termina el programa

        if opcion in ["1", "2", "3", "4"]:
            numero1, numero2 = obtener_valores()

            if opcion == "1":
                suma(numero1, numero2)
            elif opcion == "2":
                resta(numero1, numero2)
            elif opcion == "3":
                multiplicacion(numero1, numero2)
            elif opcion == "4":
                division(numero1, numero2)
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
