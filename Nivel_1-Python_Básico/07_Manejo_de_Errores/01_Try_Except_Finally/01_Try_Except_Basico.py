# Bloque try -except Básico
# Se utiliza para intentar ejecutar un bloque de código y, si ocurre un error, capturarlo y manejarlo.

try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except:
    print("Ha ocurrido un error.")

