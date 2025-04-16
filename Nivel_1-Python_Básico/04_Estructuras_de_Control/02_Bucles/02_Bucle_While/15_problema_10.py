# Escribe un while que pida al usuario ingresar "sí" o "no" y repita la pregunta hasta que ingrese una respuesta válida.

respuesta = ""
while respuesta != "si" and respuesta != "no":
    respuesta = input("Por favor, ingrese la respuesta correcta: ").strip().lower()

print("¡Has encontrado la respuesta correcta!")