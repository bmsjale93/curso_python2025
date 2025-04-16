# Crea dos funciones: una que defina una variable local y otra que intente acceder a ella(¿funciona?).

def local():
    variable = "Local"
    print("Dentro de local():", variable)

# def acceso():
#     try:
#         print("Dentro de acceso(): ", variable) # Variable no está definida aquí
#     except NameError as e:
#         print("Error: ", e)

# Llamamos a las funciones
local()
# acceso()
