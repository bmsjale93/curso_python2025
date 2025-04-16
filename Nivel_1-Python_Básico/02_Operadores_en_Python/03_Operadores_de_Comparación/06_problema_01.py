# Escribe un programa que solicite dos números al usuario y determine cuál es 
# mayor, menor o si son iguales.

# Solicitamos dos números al usuario
num1 = int(input("Por favor, introduce el primer número: "))
num2 = int(input("Por favor, introduce el primer número: "))

# Imprimimos la selección del usuario
print(f"\nUsted ha seleccionado:\nPrimer número: {num1}\nSegundo número: {num2}")

# Establecemos la condición
if num1 > num2:
    print(f"El número {num1} es mayor que el número {num2}.")
elif num1 == num2:
    print(f"Ambos números son iguales.")
else:
    print(f"El número {num2} es mayor que el número {num1}.")