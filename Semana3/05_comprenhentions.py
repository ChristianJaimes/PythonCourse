"""
Apartir de una lista de enteros generar una lista solo con los pares
"""
lista = [1,3,4,6,89,100,19,78,303]
zapatos_pares = []
for zapato in lista:
    if zapato % 2 == 0:
        zapatos_pares.append(zapato)
print(f"La lista de pares es: {zapatos_pares}")

#final = [operacin for   condicion ]
final = [x for x in lista if zapato %2 == 0]
print(f"La lista de pares es: {final}")
# Si son impares sumele uno
zapatos_impares = []
for zapato in lista:
    if zapato % 2 != 0:
        zapatos_impares.append(zapato*2)

impares_plus = [zapato*2 for zapato in lista if zapato %2 != 0] #
print(impares_plus)

