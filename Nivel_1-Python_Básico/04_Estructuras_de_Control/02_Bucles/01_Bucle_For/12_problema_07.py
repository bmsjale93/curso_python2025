# Escribe un programa que recorra un diccionario con datos personales e imprima las claves y valores.

diccionario = {"nombre": "Alejandro", "edad": 31, "trabajo": "Ingeniero"}

for clave, valor in diccionario.items():
    print(clave, ":", valor)