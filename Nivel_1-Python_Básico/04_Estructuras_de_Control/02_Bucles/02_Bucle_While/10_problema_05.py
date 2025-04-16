# Usa while para imprimir los números pares del 2 al 20.

contador = 0

while contador <= 20:
    contador += 1
    if (contador % 2 != 0):
        continue
    print(f"Número PAR: {contador}")
