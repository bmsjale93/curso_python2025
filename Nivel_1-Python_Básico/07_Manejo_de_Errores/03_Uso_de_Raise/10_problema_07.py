# Lanza un TypeError si el argumento de una función no es de tipo int.

def positivo(numero):
    print("El número ingresado es", numero)

try:
    numero = int(input("Por favor, ingrese un número: "))
    positivo(numero)
except ValueError:
    print("Error: Debes introducir un número entero.")
