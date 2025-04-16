# Escribe un programa que pida la edad y si tiene licencia de conducir. Si la edad 
# es mayor o igual a 18 y tiene licencia, imprime "Puedes conducir", de lo 
# contrario muestra "No puedes conducir".

edad = int(input("Por favor, ingresa tu edad: "))
licencia = input("¿Tiene licencia de conducir? Responda con Si o No: ").strip().lower()

if edad >= 18:
    if licencia in ["si", "sí"]:
        print("Puedes conducir.")
    else:
        print("Sin licencia no puedes conducir.")
else:
    print("Ni tienes edad ni licencia para conducir.")