# Formateo de Cadenas en print()

# Uso de f-strings(Recomendado)
# Permite incrustar variables dentro de una cadena:
nombre = "Ana"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
# Salida: Hola, mi nombre es Ana y tengo 25 años.

# Uso de .format()
# Otra opción para formatear cadenas:
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))

# Uso del % (Obsoleto, no recomendado)
print("Hola, mi nombre es %s y tengo %d años." % (nombre, edad))