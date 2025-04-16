# ¿Qué sucede con este código? Explícalo en tu respuesta:
lista = [1, 2, 3]
tupla = (1, 2, 3)

lista.append(4)  # ¿Funciona?
tupla.append(4)  # ¿Funciona?

# La tupla, al no ser modificable, generará un error al ejecutar el script. 
# Sin embargo, en la lista se añadirá correctamente al final de la misma.