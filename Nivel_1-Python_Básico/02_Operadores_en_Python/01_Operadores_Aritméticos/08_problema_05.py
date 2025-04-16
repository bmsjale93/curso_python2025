# Escribe un programa que reciba dos números del usuario y muestre la 
# suma, resta, multiplicación y división entre ellos.

# Pedimos dos número al usuario
numero_1 = input("Por favor, introduzca el primer número: ")
numero_1 = int(numero_1)    # Como nos da texto, debemos convertirlo a entero.

numero_2 = input("Por favor, introduzca el segundo número: ")
numero_2 = int(numero_2)

# Ahora, realizamos los cálculos
print("La suma de ambos números es: ", numero_1 + numero_2)
print("La resta de ambos números es: ", numero_1 - numero_2)
print("La multiplicación de ambos números es: ", numero_1 * numero_2)
print("La división de ambos números es: ", numero_1 / numero_2)