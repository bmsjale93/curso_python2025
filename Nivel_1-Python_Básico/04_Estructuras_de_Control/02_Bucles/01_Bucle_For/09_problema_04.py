# Pide al usuario una lista de 5 números y usa for para mostrar su suma.

# Solicitar 5 números y almacenarlos en una lista
numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calculamos la suma de los numeros
suma_total = 0
for numero in numeros:
    suma_total += numero

# Mostramos el resultado
print(f"La suma de los números ingresados es: {suma_total}")