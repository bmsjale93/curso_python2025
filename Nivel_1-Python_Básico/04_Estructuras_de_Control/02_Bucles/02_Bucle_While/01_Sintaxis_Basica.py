# Sintaxis de while
# El bucle while se usa cuando no sabemos cuántas veces se ejecutará el código, pero sí sabemos la condición que debe cumplirse para que continúe ejecutándose.

# EJEMPLO
contador = 1
while contador <= 5:
    print(f"Iteración {contador}")
    contador += 1   # Incremento para evitar bucles infinitos