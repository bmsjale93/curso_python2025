# Error de Conversión de Valores(ValueError)
# Se produce cuando tratamos de convertir un tipo de dato de forma incorrecta, como convertir texto que no representa un número.

try:
    numero = int(input("Introduce un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: Debes introducir un número válido.")