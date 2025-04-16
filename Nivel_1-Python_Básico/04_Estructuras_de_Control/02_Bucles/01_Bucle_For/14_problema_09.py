# Pide al usuario una frase y cuenta cuántas veces aparece la letra "a".

frase = input("Por favor, ingrese una frase: ").strip().lower()

contador = 0
for letra in frase:
    print(letra)
    if letra == "a":
        contador += 1
    else:
        continue

print(f"Ha escrito un total de {contador} aes.")