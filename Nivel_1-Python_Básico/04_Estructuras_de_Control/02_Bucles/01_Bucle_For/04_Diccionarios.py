# Uso de for con Diccionarios
# Para recorrer claves y valores de un diccionario:

persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(clave, ":", valor)