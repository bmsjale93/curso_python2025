# Usa for para encontrar el número más grande en una lista de números ingresada por el usuario.

numeros = []

for i in range(5):
    numero = int(input(f"Por favor, ingresa el número {i+1}: "))
    numeros.append(numero)

mayor_numero = 0

for numero in numeros:
    print(numero)
    if numero > mayor_numero:
        mayor_numero = numero
    else:
        continue

print(f"El número más grande ingresado es {mayor_numero}")