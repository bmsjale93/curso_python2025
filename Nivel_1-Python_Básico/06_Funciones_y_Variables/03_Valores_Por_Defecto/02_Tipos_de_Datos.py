# VALORES POR DEFECTO CON TIPOS DE DATOS COMUNES
# Los valores por defecto pueden ser:
# Números
# Cadenas de texto
# Booleanos
# Tuplas, listas, diccionarios(aunque en este caso se debe tener precaución con objetos mutables).

def agregar_elemento(lista=None):
    if lista is None:
        lista = []
    lista.append("Nuevo elemento")
    print(lista)
    return lista