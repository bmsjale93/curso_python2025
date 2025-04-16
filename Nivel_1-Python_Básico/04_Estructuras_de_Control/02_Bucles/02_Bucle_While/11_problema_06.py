# Escribe un programa que pregunte al usuario un número y sume todos los números del 1 hasta ese número.

numero = int(input("Por favor, ingrese un número: "))
contador = 0
suma_total = 0

while contador <= numero:
    print(f"Suma actual -> {suma_total} + {contador}")
    suma_total = suma_total + contador
    contador += 1
    print(f"Suma actual = {suma_total}")

print(f"La suma total es {suma_total}")