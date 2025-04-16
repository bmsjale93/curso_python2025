# Crea una función mostrar_menu(opcion="inicio") que imprima el menú dependiendo de la opción.

seleccion = input("Por favor seleccione una opción:\nInicio\nHistoria\nAjustes\n").lower().strip()

def mostrar_menu(opcion="inicio"):
    if opcion == "inicio":
        print("Mostrando el menú inicial")
    elif opcion == "historia":
        print("Iniciando Modo Historia...")
    elif opcion == "ajustes":
        print("Entrando en Ajustes...")
    else:
        print("Opción No Válida")

mostrar_menu(opcion=seleccion)