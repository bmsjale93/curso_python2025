# Declara dos variables, una con True y otra con False. Usa or y and en combinación 
# con = para asignar nuevos valores y analiza el resultado.

# Creamos ambas variables
a = True
b = False

# Usamos 'or' para asignar un nuevo valor
c = a or b
print(f"c = a or b -> {c}")     # Salida: True

# Usamos 'and' para asignar un nuevo valor
d = a and b
print(f"d = a and b -> {d}")     # Salida: False

# Usamos 'and' y 'or' juntos
e = (a and b) or a
print(f"e = (a and b) or a -> {e}")     # Salida: True
