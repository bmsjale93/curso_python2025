# Pide al usuario un número, y si no lo introduce correctamente, vuelve a pedírselo hasta que lo haga bien.

while True:
    try:
        numero = int(input("Ingresa un número: "))
        print(f"Has ingresado el número {numero}.")
        break
    except ValueError as e:
        print(f"Error: {e}")