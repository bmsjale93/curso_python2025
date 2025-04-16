# Controlando el Bucle con break
# El break permite salir del bucle incluso si la condición aún es verdadera.

while True:
    palabra = input("Escribe salir para terminar: ")
    if palabra == "salir":
        print("Saliendo del programa...")
        break

