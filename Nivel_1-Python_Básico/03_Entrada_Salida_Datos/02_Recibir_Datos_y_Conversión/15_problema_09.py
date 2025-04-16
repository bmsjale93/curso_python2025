# Crea un programa que capture una frase y cuente cuántas palabras tiene.

# Buscamos capturar una frase
frase = input("Por favor, ingrese una frase: ")

# Calculamos el número de palabras
num_palabras = len(frase.split())

# Mostramos el resultado
print(f"La frase tiene {num_palabras} palabras.")