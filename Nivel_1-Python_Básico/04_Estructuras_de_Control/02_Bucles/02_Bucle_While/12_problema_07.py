# Crea un while que cuente cuántas veces el usuario ingresa un número impar, deteniéndose si ingresa 0.

contador = 0

while True:
    numero = int(input("Por favor, ingrese un número: "))
    if ( numero % 2 != 0):
        contador += 1
    elif (numero == 0):
        break
    else:
        continue

print(f"Ha ingresado un total de {contador} números impares.")