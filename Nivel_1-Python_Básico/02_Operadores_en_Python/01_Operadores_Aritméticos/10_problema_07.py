# Usa la fórmula del interés compuesto para calcular el monto final después de t años:
# M = P * (1 + r/n) ** (n*t)

# Donde:
# P = 1000 (capital inicial)
# r = 0.05 (tasa de interés anual)
# n = 12 (número de veces que se capitaliza por año)
# t = 5 (años)

# Creamos las variables
P = 1000
r = 0.05
n = 12
t = 5

# Establecemos la fórmula
M = P * (1 + r/n) ** (n/t)

# Imprimimos el resultado
print(f"Según las condiciones dadas, el monto final es: {M:.2f}")