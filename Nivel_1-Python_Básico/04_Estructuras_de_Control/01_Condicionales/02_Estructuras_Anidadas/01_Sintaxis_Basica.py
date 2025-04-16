# Uso de Estructuras Anidadas
# Las estructuras anidadas en Python permiten incluir condicionales dentro de 
# otros condicionales (if dentro de if). Esto es útil cuando se deben evaluar 
# múltiples condiciones dependientes.

# EJEMPLO
edad = 20
tiene_identificacion = True

if edad >= 18:
    if tiene_identificacion:
        print("Acceso permitido.")
    else:
        print("Debes presentar una identificación.")
else:
    print("Eres menor de edad.")