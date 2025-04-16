# Crea una función que reciba dos números y lance un ZeroDivisionError si el segundo es cero.

def division(numerador, denominador):
    if denominador < 0:
        raise ZeroDivisionError("Error: No se puede dividir por cero.")
    return numerador / denominador

a = int(input("Numerador: "))
b = int(input("Denominador: "))

print(f"El resultado es {division(a, b)}")