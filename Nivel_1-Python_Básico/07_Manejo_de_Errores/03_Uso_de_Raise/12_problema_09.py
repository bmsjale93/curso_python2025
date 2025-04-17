# Implementa un programa que use raise para advertir cuando el usuario introduce una contraseña de menos de 6 caracteres.

class ContrasenaDebil(Exception):
    pass

def pass_debil(contrasena):
    if len(contrasena) < 6:
        raise ContrasenaDebil("\nLa contraseña es menor de 6 caracteres.")
    print("Contraseña creada correctamente.")

try:
    contrasena = input("Por favor, introduce una contraseña: ")
    pass_debil(contrasena)
except Exception as e:
    print("Se ha producido un error: ", e)