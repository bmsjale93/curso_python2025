# Pide al usuario su edad y muestra si es menor de edad, mayor de edad o 
# un adulto mayor (65 + años).

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 65:
    print("Es un adulto mayor")
elif edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
