# Define una función sumar_lista(lista) que reciba una lista de números y devuelva su suma.

def sumar_lista(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado

resultado_final = sumar_lista([2, 3, 4, 5, 6, 7, 8])
print(f"La suma total es {resultado_final}")