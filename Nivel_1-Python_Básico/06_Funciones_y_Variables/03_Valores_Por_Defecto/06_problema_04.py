# Define una función que imprima un mensaje de bienvenida y permita definir el idioma("es" por defecto).

def bienvenida(nombre, idioma="es"):
    if idioma == "es":
        print(f"Bienvenido al curso de Python, {nombre}")
    elif idioma == "en":
        print(f"Welcome to the Python Course, {nombre}")
    else:
        print("No se reconoce el idioma seleccionado.")

idioma_seleccionado = input("Por favor, selecciona un idioma ('es' o 'en'): ")

bienvenida(nombre="Alex", idioma=idioma_seleccionado)