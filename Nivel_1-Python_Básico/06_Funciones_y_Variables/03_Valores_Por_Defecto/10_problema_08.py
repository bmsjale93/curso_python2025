# Llama a una función usando argumentos nombrados en distinto orden(keyword arguments).

def crear_usuario(nombre, edad=18, pais="España"):
    print(f"Usuario: {nombre} | Edad: {edad} | Pais: {pais}")

crear_usuario(edad=30, nombre="Alex")