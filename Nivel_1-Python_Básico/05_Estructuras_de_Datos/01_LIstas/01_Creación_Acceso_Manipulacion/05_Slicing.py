# Slicing(Rebanado)
# Podemos extraer partes de una lista con lista[inicio:fin:paso].

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:6])     # [2, 3, 4, 5] (índices 2 a 5)
print(numeros[:4])      # [0, 1, 2, 3] (desde el inicio hasta el indice 3)
print(numeros[5:])      # [5, 6, 7, 8, 9] (desde el indice 5 hasta el final)
print(numeros[::2])     # [0, 2, 4, 6, 8] (cada dos elementos)
