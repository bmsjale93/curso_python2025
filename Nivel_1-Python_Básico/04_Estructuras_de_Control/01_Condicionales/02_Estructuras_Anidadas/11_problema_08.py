# Pide al usuario su peso y altura, luego calcula el IMC(peso / altura²) e indica si está en bajo peso, peso normal, sobrepeso o obesidad.

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

imc = peso / (altura * altura)
print(imc)

if imc > 18.5:
    if imc < 25:
        print("Normal.")
    elif imc < 30:
        print("Sobrepeso.")
    elif imc < 35:
        print("Obesida I.")
    elif imc < 40:
        print("Obesidad II")
    else:
        print("Obesidad III.")
else:
    print("Bajo Peso.")