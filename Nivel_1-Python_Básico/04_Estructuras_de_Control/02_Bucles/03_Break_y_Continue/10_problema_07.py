# Crea un programa que genere números aleatorios entre 1 y 100 hasta encontrar el número 50, usando break .

from random import *

contador = 0

while True:
    random = randint(1, 100)
    contador += 1
    if random == 50:
        print("¡Encontrado el Nº 50!")
        break
    print(f"Nº Random generado: {random}")

print(f"\nSe han generado un total de {contador} números aleatorios.")