# Crear una Calculadora Simple que Permita Operaciones Básicas

# Descripción
# Desarrolla un programa que solicite al usuario dos números y una operación (+, -, *, /) , y muestre el resultado correspondiente.

# Requisitos
# Validar que el usuario introduzca números válidos.
# Capturar errores como división entre cero.
# Permitir repetir el proceso si el usuario lo desea.

# Consejos
# Usa try -except para manejar errores con ValueError y ZeroDivisionError.
# Puedes usar un while para repetir la calculadora hasta que el usuario indique lo contrario.
# Considera usar una función calculadora(num1, num2, operacion).


def calculadora(num1, num2, operacion):
    if num2 < 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    suma = num1 + num2
    resta = num1 - num2
    multiplicar = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicar, division

print("Menú de la calculadora: ")
print("Introduce 1 para suma ")
print("Introduce 2 para resta ")
print("Introduce 3 para multiplicar ")
print("Introduce 4 para division ")
print("Introduce Salir para terminar ")

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    operacion = input("Introduce una operación: ")
except Exception as e:
    print("Ha sucedido un error: ", e)