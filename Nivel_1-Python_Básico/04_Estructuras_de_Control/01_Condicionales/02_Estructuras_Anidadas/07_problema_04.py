# Escribe un programa que pida un número y verifique si es divisible entre 2 y 3 al mismo tiempo.

numero = int(input("Por favor, ingresa un número: "))

if numero % 2 == 0:
    if numero % 3 == 0:
        print(f"El número {numero} es divisible por 2 y 3.")
    else:
        print(f"El número {numero} NO es divisible por 3.")
else:
    print(f"El número {numero} NO es divisible por 2.")