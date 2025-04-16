# Pide al usuario dos números y una operación(+, -, *, /) . Realiza la operación 
# y muestra el resultado.

num1, num2 = map(float, input("Por favor, ingresa dos números (separados por comas): ").split())
operacion = input("Por favor, ingresa la operación a realizar (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"La suma entre {num1} y {num2} es {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"La resta entre {num1} y {num2} es {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"La multiplicación entre {num1} y {num2} es {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = round(num1 / num2, 2)
        print(f"La división entre {num1} y {num2} es {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operación no válida. Usa +, -, * o /.")
