# Uso de continue para Saltar Iteraciones
# continue salta la iteración actual y vuelve a evaluar la condición del while .

numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue    # Salta el número 3
    print(numero)
