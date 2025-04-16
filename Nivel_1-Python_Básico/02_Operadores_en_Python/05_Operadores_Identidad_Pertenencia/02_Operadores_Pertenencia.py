# Operadores de Pertenencia ( in , not in )
# Estos operadores permiten verificar si un elemento pertenece a una 
# secuencia como listas, tuplas, cadenas o diccionarios.

# EJEMPLO
frutas = ["manzana", "pera", "naranja"]

print("manzana" in frutas)      # True (está en la lista)
print("kiwi" in frutas)         # False (no está en la lista)
print("kiwi" not in frutas)     # True (porque no está en la lista)

# USO CON CADENAS DE TEXTO
mensaje = "Hola, bienvenido a Python"
print("Python" in mensaje)      # True
print("Java" not in mensaje)    # True

# USO CON DICCIONARIOS
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}

print("nombre" in persona)      # True (clave existente)
print("Carlos" in persona)      # False (los valores no se verifican con 'in')
print("edad" not in persona)    # False (porque la clave existe)