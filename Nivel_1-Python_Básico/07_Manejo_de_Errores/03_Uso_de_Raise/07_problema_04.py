# Implementa un programa que solicite un número positivo y use raise para lanzar un error si no es positivo.

def positivo(numero):
    if numero < 0:
        raise ValueError(f"\nEl valor {numero} es negativo.")
    print("El valor introducido es ", numero)

try:
    numero = int(input("Por favor, ingresa un número: "))
    positivo(numero)
except Exception as e:
    print("Se ha producido un error: ", e)