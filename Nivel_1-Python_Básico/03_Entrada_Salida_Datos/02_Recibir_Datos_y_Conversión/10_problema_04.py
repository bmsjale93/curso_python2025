# Pide al usuario que ingrese su nombre y apellido en una sola línea, 
# luego imprímelos por separado.

# Creamos las variables
nombre, apellido = input("Por favor, ingrese su nombre y apellido (separado por espacios): ").split()

# Imprimimos los valores
print(f"Bienvenido a la clase de Python, {nombre} {apellido}.")