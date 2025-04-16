# Crea un while que solicite números al usuario y termine cuando ingrese un número negativo.

suma_total = 0
while True:
    numero = int(input("Por favor, ingresa un número: "))
    if numero < 0:
        print("Terminando la ejecución...")
        break
    suma_total = suma_total + numero
    print(f"La suma actual es {suma_total}")
