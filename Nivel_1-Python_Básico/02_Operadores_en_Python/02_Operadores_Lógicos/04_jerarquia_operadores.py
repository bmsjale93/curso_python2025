# El orden de evaluación de los operadores lógicos sigue esta prioridad:
# not (se evalúa primero).
# and (se evalúa después).
# or (se evalúa al final).

# Ejemplo
resultado = not True or False and True
print(resultado)    # Salida: False

# Explicación
# -> not True -> False
# -> False and True -> False
# -> False or False -> False

# Podemos modificar la prioridad con paréntesis
resultado = not (True or False) and True
print(resultado)    # Salida: False

# Explicación:
# -> True or False -> True
# -> not True -> False
# -> False and True -> False