# Pide al usuario que ingrese dos números y muestra su suma.

# Creamos la variable de captura
num1, num2 = map(int, input("Por favor, ingresa dos números (separados por comas): ").split())
suma = num1 + num2

# Imprimimos los valores
print(f"La suma de {num1} y {num2} es {suma}.")