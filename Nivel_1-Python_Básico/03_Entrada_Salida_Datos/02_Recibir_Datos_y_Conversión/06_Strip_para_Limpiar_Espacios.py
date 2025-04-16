# Uso de strip() para Limpiar Espacios en input()
# A veces, los usuarios ingresan espacios adicionales. 
# Se puede eliminar con .strip():

nombre = input("Ingresa tu nombre: ").strip()
print(f"Bienvenido, {nombre}")