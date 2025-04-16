# Crea un programa que solicite un número y lo divida entre 2, manejando cualquier error que ocurra.

try:
    numero = int(input("Por favor, ingresa un número: "))
    resultado = numero / 2
    print(f"Resultado: {resultado:.2f}")
except ValueError:
    print("Debes ingresar un número.")

