# Implementa un programa que capture cualquier error desconocido usando except Exception.

while True:
    try:
        a = int(input("Numerador: "))
        b = int(input("Denominador: "))
        resultado = a / b
        print(f"El resultador es {resultado}.")
        break
    except ValueError as v:
        print("Error: ", v)
    except Exception as e:
        print("Error: ", e)