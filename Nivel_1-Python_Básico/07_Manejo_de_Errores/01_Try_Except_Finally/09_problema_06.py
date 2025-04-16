# Crea un programa que convierta un string a entero y maneje los errores posibles.

try:
    numero = int("Dos")
    print(numero)
except Exception as e:
    print("se ha producido el siguiente error: ", e)
finally:
    print("Saliendo del programa.")