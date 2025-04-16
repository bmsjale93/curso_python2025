# Escribe un programa que pida al usuario su presupuesto y el precio de un producto. 
# Si tiene suficiente dinero, muestra "Compra realizada", 
# de lo contrario, "Fondos insuficientes".

precio = 2500
presupuesto = int(input("Por favor, ingrese su presupuesto: "))

if presupuesto >= precio:
    print("Compra realizada.")
else:
    print("Fondos insuficientes.")