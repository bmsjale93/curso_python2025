# Crea un programa que solicite el año de nacimiento y calcule la edad, asegurando que la entrada sea válida.

try:
    fecha_nacimiento = int(input("Introduce tu año de nacimiento: "))
    edad = 2025 - fecha_nacimiento
    print(f"Tu edad es {edad} años.")
except ValueError:
    print("Debes introducir un número válido.")
