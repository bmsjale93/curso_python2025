# Escribe una función calcular_precio_final(precio, iva) que devuelva el precio con IVA.

def calcular_precio_final(precio, iva):
    return precio + (precio * (iva/100))


precio_final = calcular_precio_final(30, 21)
print(f"El precio final es de {precio_final}")
