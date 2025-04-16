# Captura y maneja tanto un ZeroDivisionError como un ValueError en una operación de división.

try:
    entrada = input("Introduce dos números separados por un espacio: ")
    num1, num2 = map(float, entrada.split())
    numeros = [num1, num2]
    resultado = numeros[0] / numeros[1]
    print(f"El resultado de dividir {numeros[0]} entre {numeros[1]} es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Por favor, introduce dos números válidos, separados por un espacio.")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")

