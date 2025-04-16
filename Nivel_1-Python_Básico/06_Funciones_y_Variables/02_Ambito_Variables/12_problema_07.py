# Declara una variable global , crea una función que la lea pero no la modifique, y otra que la modifique con global.

variable = "Global"

def lectura(variable):
    print("Leyendo la variable: ", variable)

def modificar():
    global variable
    variable = "Modificada"
    print("Variable actual: ", variable)

lectura(variable)
modificar()