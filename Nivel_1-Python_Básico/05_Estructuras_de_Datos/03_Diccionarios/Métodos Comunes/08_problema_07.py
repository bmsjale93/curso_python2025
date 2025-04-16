# Crea un diccionario y genera una copia usando copy(). Modifica la copia y muestra que el original no cambia.

persona = {"nombre": "Alejandro", "edad": 31, "trabajo": "Ingeniero"}

copia_persona = persona.copy()
copia_persona["original"] = "No"
print(copia_persona)
print(persona)