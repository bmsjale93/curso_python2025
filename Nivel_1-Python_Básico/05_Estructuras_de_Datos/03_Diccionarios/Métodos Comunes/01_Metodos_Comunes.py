# Métodos Comunes para Modificar Diccionarios
# Python proporciona varios métodos integrados para modificar, actualizar, eliminar y gestionar los datos dentro de un diccionario. Estos métodos permiten trabajar de forma dinámica con la estructura clave-valor.

# UPDATE() -> Añadir o Actualizar Claves y Valores
# Este método permite agregar nuevas claves o actualizar valores existentes.

persona = {"nombre": "Carlos", "edad": 30}
persona.update({"edad":31})                     # Actualiza
persona.update({"ciudad": "Madrid"})            # Agrega nueva clave

print(persona)  # {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Madrid'}


# POP() -> Eliminar una CLave y Devolver su Valor
# Elimina una clave del diccionario y devuelve su valor. 
# Si no existe, lanza un error (salvo que se proporcione un valor por defecto).

persona = {"nombre": "Carlos", "edad": 30}
edad = persona.pop("edad")
print("edad")       # 30
print("persona")    # {'nombre': 'Carlos'}


# POPITEM() -> Elimina y Devuelve el último Par Clave-Valor
# Este método es útil para eliminar el último elemento insertado (en Python 3.7+).

datos = {"a": 1, "b": 2, "c": 3}
clave_valor = datos.popitem()
print(clave_valor)  # ('c', 3)
print(datos)        # {'a': 1, 'b': 2}


# DEL() -> Eliminar una Clave Específica
# Otra forma de eliminar una clave directamente.

persona = {"nombre": "Carlos", "edad": 30}
del persona["edad"]
print(persona)  # {'nombre': 'Carlos'}


# CLEAR() -> Elimina todos los Elementos del Diccionario
# Deja el diccionario vacío.

persona = {"nombre": "Carlos", "edad": 30}
persona.clear()
print(persona)  # {}


# AÑADIR NUEVAS CLAVES DIRECTAMENTE
# Además de update(), se pueden agregar nuevas claves asignando directamente su valor:

persona = {"nombre": "Carlos"}
persona["ciudad"] = "Madrid"
print(persona)  # {'nombre': 'Carlos', 'ciudad': 'Madrid'}


# COPY() -> Copiar Directamente
# Se utiliza para crear una copia independiente del diccionario.

original = {"a": 1, "b": 2}
copia = original.copy()
copia["c"] = 3

print(original) # {'a': 1, 'b': 2}
print(copia)    # {'a': 1, 'b': 2, 'c': 3 }