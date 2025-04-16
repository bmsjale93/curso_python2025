# Explica la diferencia entre is y == usando un ejemplo con listas.

# Creamos dos listas para la explicación
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]

# Hacemos las verificaciones
print(lista1 == lista2) # True (tienen los mismos valores)
print(lista1 is lista2) # False (no apuntan al mismo objeto en memoria)