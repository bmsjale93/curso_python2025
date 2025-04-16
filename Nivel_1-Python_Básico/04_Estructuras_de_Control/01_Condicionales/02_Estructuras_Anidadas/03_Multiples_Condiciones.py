# Uso de Múltiples Condiciones
# Cuando hay muchas condiciones anidadas, en lugar de usar múltiples if, 
# se pueden usar operadores lógicos ( and, or):

edad = 25
trabaja = True

if edad >= 18 and trabaja:
    print("Eres un adulto trabajador.")
elif edad >= 18 and not trabaja:
    print("Eres un adulto, pero no trabaja.")
else:
    print("Eres menor de edad.")