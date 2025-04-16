# Declara una variable global modo = "normal", y crea una función que cambie su valor a "oscuro" solo si no está ya en "oscuro".

modo = "normal"

def cambio_entorno(nuevo_modo):
    global modo
    print(f"Modo actual: {modo}")
    if modo != "oscuro":
        modo = nuevo_modo
        print("Cambiando a modo oscuro.")
    else:
        print("Ya estamos en modo oscuro")
    print(f"Modo actualizado: {modo}")

cambio_entorno("oscuro")