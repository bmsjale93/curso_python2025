# Capturas Tipos de Errores Específicos
# Puedes capturar tipos específicos de errores para manejar cada situación de manera más precisa.

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# Explicación:
# ValueError: cuando la conversión int() falla.
# ZeroDivisionError: cuando se intenta dividir por 0.
