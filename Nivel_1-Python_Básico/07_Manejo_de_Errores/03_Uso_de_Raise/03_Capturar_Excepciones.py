# Crear y Lanzar Excepciones Personalizadas (Opcional Avanzado)
# Se pueden definir nuevas clases de excepciones creando subclases de Exception:

class ErrorEdadInvalida(Exception):
    pass

def verificar_edad(edad):
    if edad < 0:
        raise ErrorEdadInvalida("Edad no válida: debe ser positiva.")

try:
    verificar_edad(-10)
except ErrorEdadInvalida as e:
    print(f"Error personalizado: {e}")