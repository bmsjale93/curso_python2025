# Explica qué sucede con el siguiente código:
lista1 = [1, 2, 3]
lista2 = lista1
print(lista1 is lista2)
lista2.append(4)
print(lista1)

# Explicación:
# Como apuntamos lista2 a lista1, ambos apuntarán al mismo objeto en memoria
# Cuando añadimos un valor ('4') a la lista2, al apuntar al mismo objeto, se
# añadirá también a la lista1
# Al imprimir la lista1 tendremos [1, 2, 3, 4]