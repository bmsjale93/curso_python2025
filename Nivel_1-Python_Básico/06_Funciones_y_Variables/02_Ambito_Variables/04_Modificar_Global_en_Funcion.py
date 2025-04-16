# MODIFICAR VARIABLES GLOBALES DESDE FUNCIONES
# Si deseas modificar una variable global dentro de una función, debes usar la palabra clave global .

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)     # 1