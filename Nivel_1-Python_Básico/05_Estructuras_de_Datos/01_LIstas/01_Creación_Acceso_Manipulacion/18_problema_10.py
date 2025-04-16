# Escribe un programa que pida 5 números al usuario, los almacene en una lista y los muestre en orden inverso.

numeros = []

while len(numeros) < 5:
    numero = int(input("Por favor, ingrese un número aleatorio: "))
    numeros.append(numero)

print(numeros)