# Crea una función convertir_a_celsius(fahrenheit) que devuelva los grados en Celsius.

def convertir_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = convertir_a_celsius(80)
print(f"{celsius:.2f} ºC")
