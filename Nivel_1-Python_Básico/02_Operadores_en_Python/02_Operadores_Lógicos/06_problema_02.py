# Crea un programa que verifique si un usuario es administrador(es_admin) o 
# tiene una suscripción premium(es_premium). Si al menos una de estas 
# condiciones es verdadera, debe mostrar el mensaje "Acceso permitido".

# Realizamos las preguntas al usuario:
es_admin = input("Es usted administrador? (Responda con True o False): ")
es_admin = bool(es_admin)

es_premium = input("Es usted usuario premium? (Responda con True o False): ")
es_premium = bool(es_premium)

# Establecemos la condición
if es_admin or es_premium:
    print("Acceso permitido.")
else:
    print("Acceso NO permitido.")

