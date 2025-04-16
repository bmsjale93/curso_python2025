# Escribe un programa que genere un número aleatorio del 1 al 10 y haga que el usuario intente adivinarlo hasta acertar.
from random import *
random = randint(0, 10)
numero = 0

while numero != random:
    numero = int(input("Ingrese un número: "))
    if numero != random:
        print("Has fallado, vuelve a probar...")

print("¡Has acertado!")