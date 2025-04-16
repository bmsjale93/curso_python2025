# Operadores de Identidad (is, is not)
# Los operadores de identidad se utilizan para comprobar si dos 
# variables apuntan al mismo objeto en memoria, no si tienen el mismo valor.

# EJEMPLO

a = [1, 2, 3]
b = [1, 2, 3]
c = a   # 'c' apunta al mismo objeto en memoria que 'a'

print(a is b)   # False (Aunque tienen los mismos valores, son objetos diferentes)
print(a is c)   # True (Ambos apuntan a la misma dirección de memoria)
print(a is not b)   # True (Porque 'a' y 'b' son diferentes en memoria)