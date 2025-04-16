# Usa finally para imprimir "Programa finalizado" sin importar si hubo error o no.

try:
    archivo = open("prueba.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Programa finalizado.")