# Crea un for anidado que imprima una tabla de multiplicar del 1 al 5.

for i in range(1, 6):
    print(f"TABLA DE MULTIPLICAR DEL {i}")
    for j in range (1, 11):
        multiplicar = i * j
        print(f"{i} x {j} = {multiplicar}")

