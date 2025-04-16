# Usa continue para imprimir solo las vocales de una palabra ingresada por el usuario.

vocales = ["a", "e", "i", "o", "u"]

entrada = input("Por favor, introduce una frase: ")

for letra in entrada:
    if letra in vocales:
        print(letra)