# Comparación de Conjuntos
# Puedes comprobar si un conjunto es subconjunto, superconjunto o si son disjuntos:

a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))        # True
print(b.issuperset(a))      # True
print(a.isdisjoint({4}))    # True