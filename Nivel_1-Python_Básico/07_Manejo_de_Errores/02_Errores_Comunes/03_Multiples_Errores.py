# Combinar Manejo de Múltiples Errores
# Podemos capturar varios errores dentro del mismo bloque try -except .

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes introducir números válidos.")
