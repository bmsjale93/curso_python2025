# Generar Excepciones Personalizadas con raise
# Puedes lanzar cualquier tipo de excepción para advertir sobre errores lógicos en tu programa:

def ingresar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Tienes {edad} años.")

ingresar_edad(25)   # Correcto
# ingresar_edad(-5) # Generará ValueError