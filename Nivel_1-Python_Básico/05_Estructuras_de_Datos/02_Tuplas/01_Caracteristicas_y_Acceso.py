# CREACIÓN DE TUPLAS
# Se crean utilizando paréntesis() o la función tuple().

# Tuplas con Números
numeros = (1, 2, 3)

# Tuplas con distintos tipos de datos
info = ("Python", 3.10, True)

# Tupla sin paréntesis (Empaquetado Implícito)
coordenadas = 40.4168, -3.7038

# Tupla con un solo elemento (requiere una coma)
tupla_un_elemento = ("dato",)   # O también: tuple(["dato"])


# ACCESO A LOS ELEMENTOS
# Se accede igual que en las listas, usando índices:

colores = ("rojo", "verde", "azul")
print(colores[0])   # rojo
print(colores[-1])  # azul


# SLICING EN TUPLAS
# Las tuplas permiten operaciones de rebanado (slicing) igual que las listas:

dias = ("lunes", "martes", "miércoles", "jueves", "viernes")
print(dias[1:4])


# INMUTABILIDAD DE LAS TUPLAS
# Una vez creada, no se puede cambiar, eliminar o agregar elementos:

colores = ("rojo", "verde", "azul")
# colores[0] = "amarillo"   # Esto produce un error


# DESEMPAQUETADO DE TUPLAS
# Se pueden asignar varios valores a la vez desde una tupla:

persona = ("Luis", 30, "Madrid")
nombre, edad, ciudad = persona

print(nombre)   # Luis
print(edad)     # 30
print(ciudad)   # Madrid


# FUNCIONES Y MÉTODOS ÚTILES
# len(tupla)            -> Devuelve el número de elementos
# tupla.count(valor)    -> Cuenta cuantas veces aparece un valor
# tupla.index(valor)    -> Devuelve el índice de la primera aparición del valor

colores = ("rojo", "verde", "rojo", "azul")

print(len(colores))             # 4
print(colores.count("rojo"))    # 2
print(colores.index("azul"))    # 3





