# Define una función calcular_precio(base, iva=21) que calcule el precio con IVA.

def calcular_precio(nombre, base, iva=21):
    precio = base + (base * iva/100)
    print(f"El precio del producto {nombre} es: {precio:.2f}€")

calcular_precio(nombre="Nintendo Switch", base=400)