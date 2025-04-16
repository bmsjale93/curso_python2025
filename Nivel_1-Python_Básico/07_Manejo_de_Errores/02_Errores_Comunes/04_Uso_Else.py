# Uso de else para Confirmar que No Hubo Errores
# El bloque else se ejecuta solo si no ocurre ninguna excepción.

try:
    numero = int(input("Introduce un número positivo: "))
    if numero < 0:
        raise ValueError("El número debe ser positivo.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Número correcto, gracias")
