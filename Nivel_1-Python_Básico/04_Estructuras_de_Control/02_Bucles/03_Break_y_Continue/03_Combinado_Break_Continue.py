# Uso Combinado de break y continue
# Ambos pueden usarse en el mismo bucle:

for i in range(1, 10):
    if i == 5:
        continue    # Salta el número 5
    if i == 8:
        break       # Detiene el bucle en el número 8
    print(i)