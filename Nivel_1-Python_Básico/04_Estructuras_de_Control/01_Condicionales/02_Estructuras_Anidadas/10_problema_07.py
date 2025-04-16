# Crea un programa que pida la hora actual(0-23) y diga si es mañana(6-11), tarde(12-17), noche(18-23) o madrugada(0-5).

hora = int(input("Por favor, ingresa la hora actual (0-23): "))

if hora > 0 and hora < 24:
    if hora < 6:
        print("Madrugada.")
    elif hora < 12:
        print("Mañana.")
    elif hora < 18:
        print("Tarde.")
    else:
        print("Noche.")
else:
    print("La hora ingresada es incorrecta.")