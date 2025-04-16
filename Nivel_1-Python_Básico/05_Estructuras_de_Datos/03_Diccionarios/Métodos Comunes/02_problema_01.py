# Crea un diccionario con un producto y su precio. Luego, usa update() para agregar el stock disponible.

producto = {"nombre_producto": "CocaCola", "precio": 0.75}
producto.update({"stock": 30})

for clave, valor in producto.items():
    print(f"{clave} = {valor}")