# Verifica si la clave "nombre" existe en el diccionario {"nombre": "Ana", "profesion": "ingeniera"}.

persona = {
    "nombre" : "Ana",
    "profesion" : "ingeniera"
}

if "nombre" in persona:
    print("La clave SI existe")
else:
    print("La clave NO existe")