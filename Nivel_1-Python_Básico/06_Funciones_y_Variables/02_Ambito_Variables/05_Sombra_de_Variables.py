# SOMBRA DE VARIABLES
# Si una variable local tiene el mismo nombre que una variable global, la local prevalece dentro de la función.

mensaje = "Global"

def prueba():
    mensaje = "Local"
    print(mensaje)  # Imprime "Local"

prueba()
print(mensaje)  # Imprime "Global"