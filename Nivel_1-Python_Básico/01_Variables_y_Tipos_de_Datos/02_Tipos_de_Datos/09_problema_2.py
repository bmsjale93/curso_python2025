# Crea una lista con los nombres de cinco frutas. Luego:
# Imprime la primera fruta.
# Agrega una nueva fruta a la lista.
# Elimina la tercera fruta.

# Creamos la lista
lista = ["Manzana", "Naranja", "Melón", "Sandía", "Cereza"]
print(lista)

# Imprimimos la primera fruta
print(lista[0])

# Agregamos una nueva fruta
lista.append("Kiwi")
print(lista)

# Eliminamos la tercera fruta
lista.remove(lista[2])  # También: lista.remove("Melón")
print(lista)