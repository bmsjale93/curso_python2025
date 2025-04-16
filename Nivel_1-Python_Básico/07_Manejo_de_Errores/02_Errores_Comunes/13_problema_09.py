# Realiza un programa que sume dos números ingresados por el usuario, manejando errores si son inválidos.

while True:
    try:
        a = int(input("Por favor, ingresa el primer número: "))
        b = int(input("Por favor, ingresa el segundo número: "))
        resultado = a + b
        print(f"El resultado de sumar {a} y {b} es {resultado}.")
        break
    except Exception as e:
        print("Error: ", e)