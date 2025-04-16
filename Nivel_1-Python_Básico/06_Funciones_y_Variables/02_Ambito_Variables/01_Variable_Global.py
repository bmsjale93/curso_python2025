# VARIABLES GLOBALES
# Una variable declarada fuera de cualquier función se considera global. Puede ser accedida desde cualquier parte del programa, incluida dentro de funciones (pero no modificada directamente sin global).

mensaje = "Hola mundo"  # Variable Global

def mostrar():
    print(mensaje)

mostrar()   # Hola mundo