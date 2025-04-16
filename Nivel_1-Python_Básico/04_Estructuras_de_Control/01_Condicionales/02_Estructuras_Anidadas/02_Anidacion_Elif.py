# Anidación con elif
# Se pueden combinar estructuras anidadas con elif para evaluar más condiciones:

nota = 85

if nota >= 90:
    print("Excelente.")
elif nota >= 70:
    if nota >= 80:
        print("Muy bien.")
    else:
        print("Bien.")
else:
    print("Reprobado.")