# Uso de break para Salir de un Bucle
# El break detiene inmediatamente la ejecución de un bucle, incluso si la condición no se ha vuelto False.

# EJEMPLO CON WHILE
contador = 1

while contador <= 10:
    print(contador)
    if contador == 5:   # Se detiene cuando llega a 5
        break
    contador += 1

# EJEMPLO CON FOR
for letra in "Python":
    if letra == "h":
        break
    print(letra)