# Define un conjunto con los números 1, 2, 3, 3, 4, 5, 5. 
# ¿Cuántos elementos tiene realmente? 
# Agrega el número 6 y elimina el 2.

# Definimos el conjunto
numeros = {1, 2, 3, 3, 4, 5, 5}
print(numeros)
print(len(numeros)) # Vemos cuántos elementos tiene realmente

# Agregamos el número 6
numeros.add(6)
print(numeros)

# Eliminamos el 2
numeros.remove(2)
print(numeros)