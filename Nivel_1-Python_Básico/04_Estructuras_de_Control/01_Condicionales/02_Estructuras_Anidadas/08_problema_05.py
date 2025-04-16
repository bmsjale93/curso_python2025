# Pide al usuario que ingrese una letra. Si es una vocal, imprime "Es una vocal". Si no, imprime "No es una vocal".

letra = input("Por favor, ingresa una letra: ").lower()

if letra in ["a", "e", "i", "o", "u"]:
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada es una consonante.")