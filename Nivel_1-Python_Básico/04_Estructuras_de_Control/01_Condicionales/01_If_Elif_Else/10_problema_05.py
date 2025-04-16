# Pide al usuario su puntaje en un examen y muestra su calificación según la siguiente escala:
# 90-100: Excelente
# 70-89: Aprobado
# 0-69: Reprobado

nota = int(input("Por favor, ingresa la nota correspondiente: "))

if nota <= 69:
    print("Reprobado.")
elif nota >= 70 and nota <= 89:
    print("Aprobado.")
else:
    print("Excelente.")

