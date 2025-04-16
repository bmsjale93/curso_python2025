# Escribe un programa que solicite al usuario su edad y verifique si es mayor de edad.

# Creamos la variable para recibir datos
edad = int(input("Por favor, ingresa tu edad: ").strip())

# Verificamos si es mayor de edad
if edad >= 18:
    print("El usuario es mayor de edad.")
else:
    print("El usuario es menor de edad.")