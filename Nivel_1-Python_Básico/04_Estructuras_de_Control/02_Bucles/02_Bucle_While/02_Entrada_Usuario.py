# Uso de while con Entrada del Usuario
# Un while puede usarse para solicitar información hasta que se ingrese un valor válido:

contraseña = "python123"
entrada = ""

while entrada != contraseña:
    entrada = input("Introduce la contraseña: ")

print("Acceso concedido.")