# Escribe un programa que solo imprima los números impares del 1 al 20, usando continue para omitir los pares.

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)