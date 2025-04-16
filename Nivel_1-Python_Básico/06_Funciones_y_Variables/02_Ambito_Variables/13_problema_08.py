# Crea un programa que use una variable global para almacenar el idioma del sistema("es" o "en"), y dos funciones que impriman un saludo según el idioma.

idioma = "es"

def saludar():
    if idioma == "es":
        print("Bienvenido")
    elif idioma == "en":
        print("Welcome")
    else:
        print("Idioma no reconocido.")

# Función para Cambiar el Idioma Global
def cambiar_idioma(nuevo_idioma):
    global idioma   # Necesario para Modificar la variable global
    idioma = nuevo_idioma

# Pruebas del programa
saludar()       # Mostraría: Bienvenido.
cambiar_idioma("en")
saludar()       # Debería mostrar: Welcome