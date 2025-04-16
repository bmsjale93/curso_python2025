# Crea una función que reciba un parámetro y lo imprima. Dentro de la función, declara una variable local con el mismo nombre y prueba cuál se muestra.

variable = "Estoy fuera de la función (Global)"

def imprimir():
    variable = "Estoy dentro de la función (Local)"
    print(variable)

imprimir()
print(variable)