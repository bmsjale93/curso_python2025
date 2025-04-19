# Crear una Calculadora Simple que Permita Operaciones Básicas

# Descripción
# Desarrolla un programa que solicite al usuario dos números y una operación (+, -, *, /) , y muestre el resultado correspondiente.

# Requisitos
# Validar que el usuario introduzca números válidos.
# Capturar errores como división entre cero.
# Permitir repetir el proceso si el usuario lo desea.

# Consejos
# Usa try -except para manejar errores con ValueError y ZeroDivisionError.
# Puedes usar un while para repetir la calculadora hasta que el usuario indique lo contrario.
# Considera usar una función calculadora(num1, num2, operacion).

def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return num1 / num2
    else:
        print("Operación no válida.")

while True:
    print("\n---Calculadora Simple---")
    print("Operaciones disponibles: +, -, *, /")
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        operacion = input("Introduce la operacion (+, -, /, *): ").strip()
        
        resultado = calculadora(num1, num2, operacion)
        print("Resultado: ", resultado)
    except ValueError as ve:
        print("Error de valor: ", ve)
    except ZeroDivisionError as ze:
        print("Error matemático: ", ze)
    except Exception as e:
        print("Se ha producido el siguiente error: ", e)
    
    repetir = input("¿Deseas hacer otra operación? (s/n): ").lower()
    if repetir != "s":
        print("¡Gracias por utilizar la calculadora!")
        break
