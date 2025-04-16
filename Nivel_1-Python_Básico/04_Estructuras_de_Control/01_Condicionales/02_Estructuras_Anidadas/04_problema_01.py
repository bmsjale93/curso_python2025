# Crea un programa que solicite un número y determine si es positivo, negativo o cero 
# utilizando una estructura anidada.

numero = int(input("Por favor, ingrese un número: "))

if numero >= 0:
    if numero == 0:
        print("El número es cero.")
    else:
        print("El número es positivo.")
else:
    print("El número es negativo.")