# Implementa un programa que lea un archivo y garantice que el archivo se cierre usando finally .

try:
    archivo = open("prueba.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
except Exception as e:
    print("Se ha producido el siguiente error: ", e)
finally:
    print("Saliendo del programa.")