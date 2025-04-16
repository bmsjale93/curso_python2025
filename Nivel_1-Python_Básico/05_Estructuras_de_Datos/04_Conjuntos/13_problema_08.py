# Usa remove() para eliminar un elemento existente y discard() para eliminar uno que no existe(sin error).

conjunto = {1, 2, 3, 4, 4, 5, 5, 6, 6}

conjunto.remove(1)
conjunto.discard(10)
print(conjunto)