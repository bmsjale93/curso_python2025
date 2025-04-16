# Escribe un programa que solicite una palabra y la imprima letra por letra.

palabra = input("Por favor, ingrese una palabra: ").strip().lower()

contador = 0
for letra in palabra:
    contador+=1
    print(letra)

print(f"\nLa palabra contiene {contador} letras.")