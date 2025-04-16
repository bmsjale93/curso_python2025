# Intenta imprimir una variable local fuera de la función donde se creó (¿qué ocurre?).

def saludar():
    nombre = "Alex"
    print(f"Bienvenido, {nombre}")

saludar()
# print(nombre)   # Genera un error