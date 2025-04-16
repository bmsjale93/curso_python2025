# Usa break para salir de un while infinito cuando el usuario escriba "salir".

while True:
    entrada = input("Ingrese una palabra o salir para acabar: ").strip().lower()
    if entrada == "salir":
        break