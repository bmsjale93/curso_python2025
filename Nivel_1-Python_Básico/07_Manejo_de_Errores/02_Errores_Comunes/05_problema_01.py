# Escribe un programa que solicite dos números y maneje el error si el segundo número es cero.

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    resultado = a / b
    print("Resultado: ", resultado)
except ValueError:
    print("Debes introducir un número.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")