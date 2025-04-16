# Funciones con Valor de Retorno
# Una función puede devolver un valor usando la palabra clave return . El valor puede almacenarse en una variable o usarse directamente.

def multiplicar(x, y):
    return x * y

resultado = multiplicar(3, 4)
print(resultado)    # 12


# return - Finaliza la Función
# Una vez que se ejecuta return, la función finaliza. Todo lo que esté debajo de return no se ejecuta.

def ejemplo():
    return "Listo"
    print("Esto no se ejecutará")

