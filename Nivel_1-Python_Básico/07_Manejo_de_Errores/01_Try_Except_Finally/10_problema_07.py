# Crea un programa que sume dos números solicitados al usuario, asegurándote de que sean válidos.

try:
    num1 = int(input("Por favor, ingrese el primer número: "))
    num2 = int(input("Por favor, ingresa el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de sumar {num1} y {num2} es {resultado}.")
except ValueError:
    print("Debes introducir un número válido.")
except Exception as e:
    print("Se ha producido el siguiente error: ", e)
finally:
    print("Saliendo del programa.")
