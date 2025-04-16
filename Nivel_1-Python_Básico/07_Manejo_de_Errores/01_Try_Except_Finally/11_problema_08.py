# Usa try -except para manejar el intento de acceso a un índice inexistente en una lista.

lista = [1, 2, 3, 4, 5, 6]

try:
    lista[10] = 10
    print(lista)
except Exception as e:
    print("Se ha producido el siguiente error: ", e)
finally:
    print("Saliendo del programa.")