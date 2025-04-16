# Escribe un programa que solicite la temperatura en grados Celsius y muestre si 
# hace frío ( < 10°C), es templado (10-25°C) o hace calor (> 25°C)

temperatura = float(input("Por favor, ingrese la temperatura actual:"))

if temperatura < 10:
    print(f"Hace bastante frío, la temperatura es de {temperatura}ºC")
elif temperatura < 25:
    print(f"Hace buen clima, la temperatura es de {temperatura}ºC")
else:
    print(f"Hace bastante calor, la temperatura es de {temperatura}ºC")
