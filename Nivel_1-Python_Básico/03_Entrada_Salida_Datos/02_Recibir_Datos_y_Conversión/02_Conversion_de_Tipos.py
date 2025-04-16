# Conversión de Tipos (Casting)
# Dado que input() siempre devuelve un str, si se necesita operar con números, 
# es necesario convertirlos.

edad = input("Ingresa tu edad: ")   # -> Recibimos un string
edad = int(edad)    # Convertimos a entero
print(f"El próximo año tendrás {edad + 1} años.")