# Escribe una condición para verificar si un número n está en el rango de 
# 10 a 50 excluyendo el 50.

# Establecemos la variable
n = int(input("Ingrese un número: "))

# Establecemos la condición
if 10 <= n < 50:
    print(f"El número {n} se encuentra en el rango establecido.")
else:
    print(f"El número {n} no se encuentra en el rango.")