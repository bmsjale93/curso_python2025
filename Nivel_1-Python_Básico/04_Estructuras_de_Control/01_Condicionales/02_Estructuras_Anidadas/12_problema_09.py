# Escribe un programa que pida un número y verifique si está en el rango de 1 a 100, en el rango de 101 a 200 o fuera de estos rangos.

numero = int(input("Por favor, ingrese un número: "))

if numero >= 1:
    if numero <= 100:
        print("El número está entre 1 y 100.")
    elif numero <= 200:
        print("El numero está entre 101 y 200.")
    else:
        print("El número está fuera de rango.")
else:
    print("El número es menor a 1, no entra en el análisis.")