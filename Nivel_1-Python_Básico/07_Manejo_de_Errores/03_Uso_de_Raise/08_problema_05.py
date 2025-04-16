# Captura un ValueError personalizado usando try -except .

def positivo(numero):
    if numero < 0:
        raise ValueError(f"\nEl valor {numero} es negativo.")
    print("El valor introducido es ", numero)

try:
    numero = int(input("Por favor, ingresa un número: "))
    positivo(numero)
except Exception as e:
    print("Se ha producido un error: ", e)