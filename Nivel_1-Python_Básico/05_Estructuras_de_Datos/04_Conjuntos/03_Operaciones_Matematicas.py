# Operaciones Matemáticas con Conjuntos
# Los conjuntos permiten realizar operaciones como unión, intersección, diferencia y diferencia simétrica.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Unión: {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersección: {3, 4}
print(a - b)    # Diferencia: {1, 2}
print(a ^ b)    # Diferencia simétrica: {1, 2, 5, 6}
