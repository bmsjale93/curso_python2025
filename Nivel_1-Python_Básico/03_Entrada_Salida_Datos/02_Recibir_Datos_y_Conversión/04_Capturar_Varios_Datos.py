# Captura de Varios Datos en una Línea
# Se pueden capturar múltiples valores usando split():

nombre, edad = input("Ingresa tu nombre y edad separados por espacio: ").split()
edad = int(edad)    # Convertimos la edad a entero
print(f"Hola {nombre}, tienes {edad} años.")