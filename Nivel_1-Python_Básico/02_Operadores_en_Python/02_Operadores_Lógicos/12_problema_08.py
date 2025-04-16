# Corrige el error en la siguiente condición:
# if not usuario_registrado and es_admin:
#     print("Acceso denegado")
# else:
#     print("Acceso permitido")


# Establecemos las variables
usuario_registrado = False
es_admin = False

# Revisamos la condición
if not usuario_registrado and not es_admin:
    print("Acceso Denegado.")
else:
    print("Acceso permitido.")