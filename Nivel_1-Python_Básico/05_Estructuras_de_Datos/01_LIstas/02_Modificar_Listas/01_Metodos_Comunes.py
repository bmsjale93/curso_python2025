# Métodos Comunes para Modificar Listas

# Python proporciona una serie de métodos integrados que permiten modificar listas de forma sencilla y eficiente. 

# Estos métodos permiten agregar, eliminar, ordenar y manipular los elementos de una lista sin necesidad de escribir estructuras complejas.

# APPEND() - Agregar un elemento al final
frutas = ["manzana", "banana"]
frutas.append("cereza")
print(frutas)   # ['manzana', 'banana', 'cereza']

# INSERT() - Inserta un elemento en una posición específica
numeros = [1, 2, 4]
numeros.insert(2, 3)    # Inserta 3 en la posición 2
print(numeros)          # [1, 2, 3, 4]

# EXTEND() - Agrega múltiples elementos al final
colores = ["rojo", "verde"]
colores.extend(["azul", "amarillo"])
print(colores)  # ['rojo', 'verde', 'azul', 'amarillo']

# REMOVE()- Elimina el Primer Elemento con un Valor Específico
nombres = ["Ana", "Luis", "Ana"]
nombres.remove("Ana")
print(nombres)  # ["Luis", "Ana"]

# POP() - Elimina y devuelve un elemento en una posición
edades = [25, 30, 35]
valor = edades.pop(1)
print(valor)    # 30
print(edades)   # [25, 35]

# CLEAR() - Elimina todos los elementos
datos = [1, 2, 3]
datos.clear()
print(datos)    # []

# SORT() - Ordena los elementos de menor a mayor
numeros = [5, 2, 9, 1]
numeros.sort()
print(numeros)  # [1, 2, 5, 9]

# Para ordenar de forma descendente
numeros.sort(reverse=True)
print(numeros)  # [9, 5, 2, 1]

# SORTED() - Devuelve una nueva lista ordenada (sin modificar la original)
numeros = [3, 1, 4, 2]
nueva = sorted(numeros)
print(nueva)    # [1, 2, 3, 4]
print(numeros)  # [3, 1, 4, 2]

# REVERSE() - Invierte el orden de los elementos
letras = ["a", "b", "c"]
letras.reverse()
print(letras)   # ["c", "b", "a"]

# INDEX() - Devuelve el índice del primer elemento con un valor específico
numeros = [10, 20, 30]
posicion = numeros.index(20)
print(posicion) # 1

# COUNT() - Cuenta cuantas veces aparece un valor
vocales = ["a", "e", "i", "a", "o"]
print(vocales.count("a"))   # 2