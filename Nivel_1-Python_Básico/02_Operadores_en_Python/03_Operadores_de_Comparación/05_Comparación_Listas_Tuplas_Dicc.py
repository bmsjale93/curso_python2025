# Comparación entre Listas, Tuplas y Diccionarios
# Python permite comparar listas y tuplas elemento a elemento.

# EJEMPLO
print([1, 2, 3] == [1, 2, 3])   # True
print((1, 2, 3) < (1, 3, 2))    # True (Se compara posición por posición)

# Sin embargo, los diccionarios NO se pueden comparar directamente.
dic1 = {"a": 1, "b": 2}
dic2 = {"a": 1, "b": 2}
print(dic1 == dic2)     # True (Si tienen los mismos pares clave-valor)

# Pero esto generaría un error:
print(dic1 < dic2)  # TypeError
