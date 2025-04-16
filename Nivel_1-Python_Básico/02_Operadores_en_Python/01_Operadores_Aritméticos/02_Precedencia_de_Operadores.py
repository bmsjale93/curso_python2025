# PRECEDENCIA DE OPERADORES
# Cuando se combinan varios operadores en una expresión, 
# Python sigue un orden de prioridad:

# Paréntesis()
# Exponente **
# Multiplicación, División y Módulo * , /, //, %
# Suma y Resta + , -

resultado = 10 + 3 * 2      # Multiplicación antes que la suma
print(resultado)            # Salida: 16

resultado = (10 + 3) * 2    # Paréntesis alteran la prioridad
print(resultado)            # Salida: 26