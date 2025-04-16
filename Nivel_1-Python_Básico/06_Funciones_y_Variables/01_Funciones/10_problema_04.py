# Define una función mayor(a, b) que devuelva el mayor de dos números.

def mayor(a, b):
    if a > b:
        print(f"El número {a} es mayor que el número {b}")
    elif a < b:
        print(f"El número {b} es mayor que el número {a}")
    else:
        print("Ambos números son iguales")

mayor(28, 16)