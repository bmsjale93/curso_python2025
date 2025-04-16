# Crea un programa que pida el nombre de usuario y su contraseña. 
# Si el usuario es "admin" y la contraseña es "1234", muestra "Acceso concedido", 
# de lo contrario "Acceso denegado".

usuario, contraseña = input("Por favor, ingrese el nombre de usuario y la contraseña: ").split()

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")