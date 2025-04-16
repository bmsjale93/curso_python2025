# Crea un while que cuente cuántos intentos necesita un usuario para adivinar un número secreto, deteniéndose con break cuando lo acierte.

from random import *

random = randint(1, 10)
contador = 0

while True:
    numero = int(input("Ingrese un número: "))
    contador += 1
    if numero == random:
        print("Has encontrado el número secreto.")
        break

print(f"Has necesitado un total de {contador} intentos.")