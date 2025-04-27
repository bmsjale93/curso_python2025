# Generar una Contraseña Aleatoria utilizando la Biblioteca random

# Descripción
# Crea un generador de contraseñas aleatorias que incluya letras(mayúsculas y minúsculas), números y símbolos.

# Requisitos
# Usar la biblioteca random y string.
# Permitir al usuario elegir la longitud de la contraseña.
# Mostrar la contraseña generada por pantalla.

# Consejos
# Usa import random y import string.
# Puedes combinar:
# string.ascii_letters  # letras A-Z y a-z
# string.digits         # números 0-9
# string.punctuation    # símbolos como !, @, #

# Usa random.choices(conjunto, k=longitud) o random.sample().

import random
import string

# Pedimos al usuario la longitud de la contraseña
longitud = int(input("Introduce la longitud de la contraseña que deseas: "))

# Definir el conjunto de caracteres posibles
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generar la contraseña
contraseña = ''.join(random.choices(caracteres, k=longitud))

# Mostrar la contraseña generada
print(f"\nTu contraseña aleatoria es: {contraseña}")