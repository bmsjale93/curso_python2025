# Métodos Comunes con Conjuntos

# add(elem)     ->  Añade un elemento al conjunto
# remove(elem)  ->  Elimina un elemento(lanza error si no existe)
# discard(elem) ->  Elimina un elemento(sin error si no existe)
# clear()       ->  Elimina todos los elementos
# copy()        ->  Devuelve una copia del conjunto


# EJEMPLO
colores = {"rojo", "azul"}
colores.add("verde")
colores.discard("naranja")  # No lanza error
print(colores)