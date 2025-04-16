# Crea un diccionario con información sobre una persona(nombre, edad, ciudad). 
# Luego, cambia la ciudad y agrega una nueva clave llamada ocupación.

# Creamos el diccionario
persona = {
    "nombre" : "Juan",
    "edad" : 20,
    "ciudad" : "Sevilla"
}

print(persona)

# Cambiamos la ciudad
persona["ciudad"] = "Madrid"
print(persona)

# Agregamos una nueva clave
persona["ocupación"] = "Barrendero"
print(persona)