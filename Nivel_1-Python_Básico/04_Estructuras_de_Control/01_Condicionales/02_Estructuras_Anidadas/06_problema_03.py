# Pide al usuario tres números y determina si forman un triángulo válido
# (la suma de dos lados debe ser mayor que el tercero).

num1, num2, num3 = map(int, input("Por favor, ingresa 3 números que formen un triángulo (separados por espacios): ").split())

if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("Es un triángulo válido.")
else:
    print("No es un triángulo válido.")