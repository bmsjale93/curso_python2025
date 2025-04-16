# Evalúa la siguiente expresión y explica el resultado:
# resultado = 10 + 2 * 3 ** 2 - 8 // 3
# print(resultado)

resultado = 10 + 2 * 3 ** 2 - 8 // 3
print(resultado)    # Salida: 26

# Según la precedencia de operadores:
# -> Exponente: 3 ** 2 = 9
# -> Multiplicación: 2 * 9 = 18
# -> División entera: 8 // 3 = 2
# Nos quedaría: 10 + 18 - 2 = 26