# CONVERSIÓN EXPLÍCITA

# int(x) -> Convierte x a entero, eliminando los decimales.
# float(x) -> Convierte x a número flotante.
# str(x) -> Convierte x a cadena de texto.
# bool(x) -> Convierte x a True o False.
# list(x) -> Convierte x en una lista.
# tuple(x) -> Convierte x en una tupla.
# set(x) -> Convierte x en un conjunto.
# dict(x) -> Convierte x en un diccionario(requiere pares clave-valor).

# CONVERSIÓN MANUAL (DECIMAL A ENTERO)
numero_decimal = 9.99
numero_entero = int(numero_decimal)

print(numero_entero)    # Salida: 9
print(type(numero_decimal)) # Salida: class int

# CONVERSIÓN DE CADENAS A NÚMEROS
edad_texto = "25"
edad_numero = int(edad_texto)

print(edad_numero)  # Salida: 25
print(type(edad_numero))    # Salida: class int

# Si la cadena no es un número válido, puede generar error:
# int("Hola") # Esto generará un error


# CONVERSIÓN DE NÚMERO A CADENAS
numero = 100
texto = str(numero)

print(texto)    # Salida: "100"
print(type(texto))  # Salida: class str

# Esto puede ser útil cuando queremos concatenar números con texto
edad = 30
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)


# CONVERSIÓN ENTRE COLECCIONES (LISTA A TUPLA)
lista_nombres = ["Ana", "Carlos", "Elena"]
tupla_nombres = tuple(lista_nombres)

print(tupla_nombres)
print(type(tupla_nombres))

# CONVERSIÓN ENTRE COLECCIONES (LISTA A CONJUNTO -> Elimina duplicados)
lista_numeros = [1, 2, 3, 3, 4, 4, 5, 6]
conjunto_numeros = set(lista_numeros)

print(conjunto_numeros)
print(type(conjunto_numeros))

# CONVERSIÓN ENTRE COLECCIONES (LISTA A DICCIONARIO -> Pares Clave-Valor)
pares = [("nombre", "Luis"), ("edad", 28)]
diccionario = dict(pares)

print(diccionario)
print(type(diccionario))