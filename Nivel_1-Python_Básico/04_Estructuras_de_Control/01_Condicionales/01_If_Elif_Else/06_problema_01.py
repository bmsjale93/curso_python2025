# Escribe un programa que solicite al usuario un número y determine si es positivo, negativo o cero.

numero = int(input("Por favor, ingrese un número: "))

if numero < 0:
    print(f"El número {numero} es negativo.")
elif numero > 0:
    print(f"El número {numero} es positivo.")
else:
    print(f"El número ingresado es cero.")