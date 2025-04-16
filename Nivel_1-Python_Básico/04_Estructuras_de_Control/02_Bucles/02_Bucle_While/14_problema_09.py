# Usa while para encontrar el primer número divisible entre 7 y 5 mayor que 100.

contador = 100

while contador % 5 != 0 or contador % 7 != 0:
    contador += 1
    print(f"Contador actual: {contador}")

print(f"El primer número divisible entre 5 y 7, superior a 100 es {contador}")