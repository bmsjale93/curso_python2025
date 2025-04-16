# Escribe una función que reciba una lista como parámetro opcional y agregue "nuevo" solo si no recibe ninguna lista.

def agregar_elemento(lista=None):
    if lista is None:
        lista = []
        lista.append("Nuevo elemento")
    print(lista)

agregar_elemento()