# Agregar y Eliminar Elementos
# Podemos agregar elementos con append(), insert() y extend().

frutas = ["manzana", "banana"]

# AGREGAR ELEMENTOS
frutas.append("uva")                # Agrega uva al final
frutas.insert(1, "pera")            # Inserta pera en la posición 1
frutas.extend(["naranja", "kiwi"])  # Agrega múltiples elementos

print(frutas)   # ["manzana", "pera", "banana", "uva", "naranaja", "kiwi"]

# ELIMINAR ELEMENTOS
frutas.remove("pera")   # Elimina pera
frutas.pop(2)           # Elimina el elemento en el índice 2
del frutas[-1]          # Elimina el último elemento

print(frutas)   # ["manzana", "banana", "naranaja"]
