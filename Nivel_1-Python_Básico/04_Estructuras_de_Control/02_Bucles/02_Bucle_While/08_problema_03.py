# Escribe un programa que solicite una contraseña y no termine hasta que el usuario ingrese "secreto".

passwd = "secreto"
entrada = ""

while passwd != entrada:
    entrada = input("Por favor, ingresa la contraseña: ")

print("Acceso concedido.")