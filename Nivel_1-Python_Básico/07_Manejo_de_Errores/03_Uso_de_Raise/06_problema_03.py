# Define una función que reciba una edad y lance un error si la edad es negativa o mayor de 120.

def comprobar_edad(edad):
    if edad > 120 or edad < 0 :
        raise ValueError("Error: Has introducido un valor incorrecto.")
    año_nacimiento = 2025 - edad
    print(f"Naciste en el año {año_nacimiento}")

try:
    edad = int(input("Ingresa tu edad actual: "))
    comprobar_edad(edad)
except ValueError as e:
    print(e)
