# Creación de Diccionarios
# Se crean usando llaves {} o la función dict().

persona = {
    "nombre" : "Carlos",
    "edad" : 30,
    "ciudad" : "Madrid"
}

# Usando la función dict()
vehiculo = dict(marca="Toyota", modelo="Corolla", año="2020")


# ACCESO A VALORES POR CLAVE
# Se accede al valor mediante su clave, no mediante índices numéricos.
print(persona["nombre"])    # Carlos
print(persona["edad"])      # 30

# Usando la función get() para evitar errores si la clave no existe
print(persona.get("ciudad"))    # Madrid
print(persona.get("profesion")) # None (no lanza error)


# VERIFICAR EXISTENCIA DE CLAVES
# Puedes comprobar si una clave existe usando in
if "edad" in persona:
    print("La clave 'edad' existe")


# RECORRER UN DICCIONARIO
# Se pueden recorrer las claves, valores o ambos:

# Recorrer claves
for clave in persona:
    print(clave)

# Recorrer valores
for valor in persona.values():
    print(valor)

# Recorrer claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")


# DICCIONARIOS ANIDADOS
# Un diccionario puede contener otros diccionarios:
usuarios = {
    "usuario1": {"nombre": "Ana", "edad": 28},
    "usuario2": {"nombre": "Luis", "edad": 35}
}

print(usuarios["usuario1"]["nombre"])   # Ana


# LONGITUD DEL DICCIONARIO
# Para saber cuántos pares clave-valor tiene un diccionario:
print(len(persona)) # 3