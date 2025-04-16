# Usa try -except para evitar errores cuando el usuario ingrese 
# texto en lugar de un número.

try:
    num1 = int(input("Por favor ingresa un número: "))
    print(f"El doble del número {num1} es {num1 * 2}")
except ValueError:
    print("Error: Ingresa un número válido.")