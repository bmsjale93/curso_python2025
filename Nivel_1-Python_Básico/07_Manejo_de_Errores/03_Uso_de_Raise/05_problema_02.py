# Escribe una función validar_nombre(nombre) que lance un ValueError si el nombre está vacío.

def validar_nombre(nombre):
    if nombre == "":
        raise ValueError("Error: El nombre está vacío")
    return print(f"Bienvenido, {nombre}")

usuario = input("Ingresa tu nombre de usuario: ")
validar_nombre(usuario)