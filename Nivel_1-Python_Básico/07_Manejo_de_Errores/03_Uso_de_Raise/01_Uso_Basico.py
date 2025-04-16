# Uso Básico de raise
# Lanzar una excepción de tipo estándar:

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

print(dividir(10, 2))   # 5.0
# print(dividir(10, 0)) # Generará ZeroDivisionError