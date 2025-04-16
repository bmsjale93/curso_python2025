# Escribe un programa que intente convertir una cadena a flotante, capturando posibles errores.

try:
    float = float(input("Introduce un número: "))
    print(f"Has introducido el número: {float:.2f}")
except ValueError as e:
    print(f"Error: {e}")