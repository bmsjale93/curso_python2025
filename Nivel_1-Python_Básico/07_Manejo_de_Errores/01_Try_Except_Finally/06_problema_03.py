# Crea un programa que intente abrir un archivo inexistente y maneje el error con un mensaje.

try:
    archivo = open("prueba.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Intentamos cerrar el archivo...")
    archivo.close()

