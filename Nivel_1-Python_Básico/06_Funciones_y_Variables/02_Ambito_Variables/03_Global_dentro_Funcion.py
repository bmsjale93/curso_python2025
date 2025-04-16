# VARIABLES GLOBALES DENTRO DE FUNCIONES (LECTURA)
# Puedes leer una variable global dentro de una función sin necesidad de declararla como global, siempre que no intentes modificarla:

mensaje = "Bienvenido"

def mostrar_mensaje():
    print(mensaje)  # Correcto

mostrar_mensaje()