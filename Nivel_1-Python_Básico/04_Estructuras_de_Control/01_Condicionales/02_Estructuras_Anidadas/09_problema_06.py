# Escribe un programa que solicite el ingreso de un usuario y una contraseña. Si el usuario es "admin" y la contraseña es "1234", muestra "Acceso concedido". Si el usuario es correcto pero la contraseña es incorrecta, muestra "Contraseña incorrecta". Si el usuario es incorrecto, muestra "Usuario no registrado".

usuario = input("Por favor, ingresa un nombre de usuario: ")
contrasena = input("Por favor, ingresa la contraseña: ")

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")
    else:
        print("No ha ingresado la contraseña correcta.")
else:
    print("El nombre de usuario no existe.")