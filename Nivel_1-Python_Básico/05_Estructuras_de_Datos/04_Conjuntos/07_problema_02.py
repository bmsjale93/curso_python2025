# Convierte una lista con duplicados[1, 1, 2, 3, 3] en una lista sin duplicados.

lista = (1, 2, 2, 2, 3, 4, 4, 4, 5, 5)
print(type(lista))

lista_sin_duplicados = list(set(lista))
print(type(lista_sin_duplicados))
print(lista_sin_duplicados)