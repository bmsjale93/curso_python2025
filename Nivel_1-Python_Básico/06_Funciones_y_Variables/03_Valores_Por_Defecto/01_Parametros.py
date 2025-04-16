# DEFINIR PARÁMETROS CON VALORES POR DEFECTO 
# Se asigna un valor inicial al parámetro directamente en la definición de la función.

def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

# Llamadas posibles
saludar("Ana")  # Hola, Ana
saludar()       # Hola, invitado


# COMBINACIÓN DE PARÁMETROS OBLIGATORIOS Y OPCIONALES
# Se pueden mezclar parámetros obligatorios y parámetros con valor por defecto, siempre respetando el orden: primero los obligatorios, después los opcionales.

def describir_persona(nombre, edad=30, ciudad="Desconocida"):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# Ejemplos de llamada
describir_persona("Carlos")                 # Carlos tiene 30 años y vive en Desconocida
describir_persona("Ana", 25, "Sevilla")     # Ana tiene 25 años y vive en Sevilla


# USAR PALABRAS CLAVE
# Se puede llamar a la función especificando los argumentos por nombre, sin seguir necesariamente el orden:
describir_persona(nombre="Luis", ciudad="Madrid")   # Luis tiene 30 años y vive en Madrid.