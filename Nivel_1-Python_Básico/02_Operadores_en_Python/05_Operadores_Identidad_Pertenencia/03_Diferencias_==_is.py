# Diferencias entre is y ==

# EJEMPLO
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)   # True (mismo contenido)
print(x is y)   # False (diferentes objetos en memoria)
print(x is z)   # True (misma referencia en memoria)