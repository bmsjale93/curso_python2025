# Crea una excepción personalizada ErrorValorNegativo y úsala si un número ingresado es negativo.

class ErrorValorNegativo(Exception):
    pass

def positivo(numero):
    if numero < 0:
        raise ErrorValorNegativo("\nEl número introducido es negativo.")
    print("El número ingresado es ", numero)

try:
    numero = int(input(f"Por favor, ingrese un numero: "))
    positivo(numero)
except Exception as e:
    print("Se ha producido un error: ", e)