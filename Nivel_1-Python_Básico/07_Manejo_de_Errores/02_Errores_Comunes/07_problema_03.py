# Pide dos números al usuario y realiza su división manejando ambos errores (ValueError y ZeroDivisionError).

try:
    a = int(input("Introduce el numerador: "))
    b = int(input("Introduce el denominador: "))
    resultado = a / b
    print("Resultado: ", resultado)
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
