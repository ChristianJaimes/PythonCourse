def suma_dos_numeros(x, y):  # x = 4 y y = 5
    r = x + y
    print(f"El resultado de la operacion es: {r}")

def restar_dos_numeros(x, y):
    r = x - y
    print(f"El resultado de la operacion es: {r}")


def multiplicar_dos_numeros(x, y):
    r = x * y
    print(f"El resultado de la operacion es: {r}")

def dividir_dos_numeros(x,y):
    r = x / y 
    print(f"El resultado de la operacion es: {r}")

def mostrar_menu():
      print("calculadora basica")
      print("""
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Salir
            """)
      
def ingreso_de_datos():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    return numero1,numero2
if __name__ == "__main__":
    mostrar_menu()
    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        a,b = ingreso_de_datos()
        suma_dos_numeros(a,b)
    elif opcion == 2:
        a,b = ingreso_de_datos()
        restar_dos_numeros(a,b)
    elif opcion == 3:
        a,b = ingreso_de_datos()
        multiplicar_dos_numeros(a,b)
    elif opcion == 4:
        a,b = ingreso_de_datos()
        dividir_dos_numeros(a,b)
    elif opcion == 5:
        print("Hasta luego")
else:
    print("Error numero no valido")
