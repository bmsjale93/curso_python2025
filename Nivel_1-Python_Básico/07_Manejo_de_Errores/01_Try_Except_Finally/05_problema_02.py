# Escribe un programa que solicite un número entero y maneje correctamente si el usuario escribe texto.

try:
    numero = int(input("Por favor, ingresa un número: "))
    print(f"Has ingresado el número {numero}")
except ValueError:
    print("Debes ingresar un número.")


