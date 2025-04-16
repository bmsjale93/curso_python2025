# Pide al usuario que ingrese un número y muestra si es par o impar.

# Creamos la variable para pedir el número
num = int(input("Por favor, ingrese un número: "))

# Verificamos si es par o impar
if num % 2 == 0:
    print("El número es PAR.")
else:
    print("El número es IMPAR.")