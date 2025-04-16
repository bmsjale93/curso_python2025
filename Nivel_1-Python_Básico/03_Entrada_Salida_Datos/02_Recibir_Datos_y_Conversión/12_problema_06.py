# Pide al usuario que ingrese su peso en kg y altura en metros, luego calcula 
# su IMC(peso / altura²).

# Creamos las variables
peso, altura = map(float, input("Por favor, ingresa tu peso (kg) y altura (m) separadas por espacios: ").split())

# Creamos el calculo del IMC
imc = peso / (altura ** 2)

# Imprimimos los valores
print(f"Tu Indice de Masa Corporal es: {imc:.2f}")