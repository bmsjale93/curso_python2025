# Error de División por Cero(ZeroDivisionError)
# Este error ocurre cuando intentamos dividir un número entre 0, lo cual no es matemáticamente posible.

try:
    a = int(input("Introduce el numerador: "))
    b = int(input("Introduce el denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
