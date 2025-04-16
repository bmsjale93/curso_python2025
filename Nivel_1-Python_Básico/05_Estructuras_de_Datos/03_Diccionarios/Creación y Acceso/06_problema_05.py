# Recorre un diccionario e imprime todas las claves y valores.

semana = {
    "lunes" : 1,
    "martes" : 2,
    "miercoles" : 3,
    "jueves" : 4,
    "viernes" : 5,
    "sabado" : 6,
    "domingo" : 7
}

for clave, valor in semana.items():
    print(f"{clave} -> {valor}")