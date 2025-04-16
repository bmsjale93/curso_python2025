# Crea una función saludar_varias_veces(nombre, veces) que salude varias veces al nombre dado.

def saludar_varias_veces(nombre, veces):
    for _ in range(veces):
        print(f"Hola, {nombre}")

saludar_varias_veces("Alex", 3)

