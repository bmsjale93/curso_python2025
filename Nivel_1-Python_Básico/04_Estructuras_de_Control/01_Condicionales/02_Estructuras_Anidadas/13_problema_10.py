# Crea un programa que simule una máquina expendedora. Pide el dinero ingresado y el precio del producto. Si el dinero es suficiente, muestra "Compra realizada" y da el cambio. Si no, muestra "Fondos insuficientes".

# Definimos los productos y sus precios
productos = {
    "coca cola": 19.99,
    "fanta": 24.99
}

# Pedimos el producto al usuario
producto = input("Por favor, ingrese el producto deseado (Coca Cola o Fanta): ").strip().lower()

# Verificamos si el producto está en la lista
if producto in productos:
    precio = productos[producto]
    print(f"Has seleccionado {producto.capitalize()}")
    
    # Pedimos el dinero al usuario
    dinero = float(input(f"Por favor, ingrese la cantidad de dinero (€): "))
    
    # Verificamos que el dinero es suficiente
    if dinero < precio:
        print("Fondos insuficientes.")
    else:
        cambio = dinero - precio
        print(f"Compra realizada. Su cambio es de {cambio:.2f} €.")
else:
    print("El producto seleccionado no existe.")