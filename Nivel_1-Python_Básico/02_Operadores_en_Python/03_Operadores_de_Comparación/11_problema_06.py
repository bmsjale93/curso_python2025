# Crea una comparación encadenada para verificar si un número está en el 
# rango de 100 a 200, incluyendo ambos extremos.

# Pedimos un número al usuario
numero = int(input("Por favor, ingresa un número: "))

# Realizamos la condición
if 100 <= numero <= 200:
    print("El número está en el rango entre 100 y 200.")
else:
    print("El número no está en el rango.")