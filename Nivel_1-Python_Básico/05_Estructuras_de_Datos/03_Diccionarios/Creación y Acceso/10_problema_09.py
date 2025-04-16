# Declara un diccionario con 3 productos y sus precios. Imprime el precio de uno de ellos.

mercado = {
    "producto1" : {"nombre": "Cocacola", "precio": 1.99},
    "producto2" : {"nombre": "Oreo", "precio": 2.20},
    "producto3" : {"nombre": "Chicharrones", "precio": 4.00}
}

for clave, valor in mercado.items():
    print(f"Producto -> {clave} = {valor}")