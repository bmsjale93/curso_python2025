# Escribe un programa que solicite tres números y determine cuál es el mayor.

num1, num2, num3 = map(int, input(
    "Por favor, ingresa 3 números (separados por espacios): ").split())

if num1 > num2 and num1 > num3:
    print(f"El número {num1} es el mayor.")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es el mayor.")
else:
    print(f"El número {num3} es el mayor.")