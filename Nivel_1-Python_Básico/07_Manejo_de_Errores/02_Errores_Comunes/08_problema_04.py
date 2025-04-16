# Escribe un programa que pida un número positivo y use raise si el número es negativo.

try:
    numero = int(input("Introduce un número: "))
    if numero < 0:
        raise ValueError("El número debe ser positivo.")
except ValueError as e:
    print("Error: ", e)
else:
    print("Número correcto, gracias.")