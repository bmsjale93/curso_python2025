# VARIABLES LOCALES
# Una variable declarada dentro de una función solo existe dentro de esa función.

def saludar():
    nombre = "Ana"  # Variable Local
    print("Hola", nombre)

saludar()
# print(nombre) -> Esto generaría un error: NameError

