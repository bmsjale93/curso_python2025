# Crea una variable con una cadena de texto y usa operaciones de cadenas para:
# Convertirla en mayúsculas.
# Contar cuántas veces aparece la letra a.
# Obtener los primeros tres caracteres.

cadena = "Hola Mundo, esto es un script de Python"

# Convertimos el texto en mayúsculas
texto_mayusculas = cadena.upper()
print("Texto en mayúsculas: ", texto_mayusculas)

# Contamos cuantas veces aparece la letra a
contador_a = cadena.count('a')
print(f"La letra 'a' aparece {contador_a} veces.")

# Obtenemos los primeros tres caracteres
primeros_tres = cadena[:3]
print("Primeros tres caracteres: ", primeros_tres)