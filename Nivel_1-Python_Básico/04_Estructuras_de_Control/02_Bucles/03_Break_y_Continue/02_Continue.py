# Uso de continue para Saltar una Iteración
# El continue omite el resto del código en la iteración actual y pasa a la siguiente.

# EJEMPLO CON WHILE
numero = 0

while numero < 10:
    numero += 1
    if numero == 5:
        continue    # Salta la impresión del número 5
    print(numero)

# EJEMPLO CON FOR
for numero in range(1, 11):
    if numero % 2 == 0:
        continue    # Salta los números pares
    print(numero)