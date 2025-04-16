# Declara una variable global contador = 0, crea una función que la incremente usando global .

contador = 0

def contar():
    global contador
    contador += 1

contar()
print(contador)