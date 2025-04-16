# Usa get() para intentar acceder a una clave que no existe sin que se genere un error.

persona = {
    "nombre" : "Alejandro",
    "edad" : 30,
    "ciudad" : "Sevilla"
}

print(persona.get("trabajo"))