# Usar finally para Código que Siempre se Ejecuta
# El bloque finally se ejecuta siempre, ocurra o no una excepción. Se utiliza para liberar recursos, cerrar archivos o realizar acciones finales necesarias.

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Intentando cerrar el archivo...")
    archivo.close()

