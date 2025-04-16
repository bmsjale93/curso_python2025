# Pide al usuario una lista de números y usa break para detenerse si ingresa un número negativo.

lista = []

while True:
    numero = int(input("Por favor, ingrese un número en la lista: "))
    if numero < 0:
        break
    lista.append(numero)

print(f"Los números ingresados han sido: {lista}")