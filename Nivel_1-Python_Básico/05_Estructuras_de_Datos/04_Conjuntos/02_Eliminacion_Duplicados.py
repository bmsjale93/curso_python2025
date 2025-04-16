# Eliminación Automática de Duplicados
# Cuando se crea un conjunto con elementos duplicados, sólo se conserva una ocurrencia de cada valor.

valores = {1, 2, 2, 3, 3, 3}
print(valores)  # {1, 2, 3}

#  También se puede usar set() para eliminar duplicados de una lista
lista = [1, 2, 2, 3, 4, 4]
sin_duplicados = list(set(lista))
print(sin_duplicados)   # [1, 2, 3, 4] (El orden puede variar)