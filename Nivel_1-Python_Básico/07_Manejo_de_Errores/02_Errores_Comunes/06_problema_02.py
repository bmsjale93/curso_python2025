# Crea un programa que convierta una entrada del usuario a entero, manejando si el usuario introduce texto.

try:
    numero = int(input("Introduce un número: "))
    print(f"Has introducido el número {numero}")
except ValueError:
    print("Debes introducir un número.")
