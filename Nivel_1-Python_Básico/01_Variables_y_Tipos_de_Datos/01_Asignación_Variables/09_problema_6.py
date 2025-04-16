# Declara una constante llamada GRAVEDAD_TERRESTRE y asígnale el valor 9.81. 
# Luego, intenta reasignarle otro valor y observa qué sucede.

# Declaramos la constante
GRAVEDAD_TERRESTRE = 9.81
print("Valor inicial de GRAVEDAD_TERRESTRE: ", GRAVEDAD_TERRESTRE)

# Intentamos reasignarle otro valor
GRAVEDAD_TERRESTRE = 10.5
print("Valor modificado de GRAVEDAD_TERRESTRE: ", GRAVEDAD_TERRESTRE)

# ¿Qué sucede?

# Python permite la reasignación de GRAVEDAD_TERRESTRE sin generar un error.

# Sin embargo, esto no es recomendable, ya que el uso de mayúsculas indica que la 
# variable debería tratarse como una constante y no modificarse.
