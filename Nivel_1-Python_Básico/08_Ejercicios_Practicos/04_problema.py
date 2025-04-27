# Contar la Cantidad de Vocales en una Frase Ingresada por el Usuario

# Descripción
# Solicita una frase al usuario y cuenta cuántas vocales(a, e, i, o, u) contiene, sin importar si son mayúsculas o minúsculas.

# Requisitos
# Usar un bucle para recorrer la cadena.
# Convertir la frase a minúsculas para simplificar la búsqueda.
# Mostrar el número total de vocales encontradas.

# Consejos
# Puedes usar un conjunto vocales = {'a', 'e', 'i', 'o', 'u'} y verificar si cada carácter pertenece al conjunto.
# Usa un contador para llevar la cuenta.
# También puedes mostrar cuántas veces aparece cada vocal si quieres ampliar el ejercicio.

from collections import Counter

vocales = {'a', 'e', 'i', 'o', 'u'}

# Pedimos la frase al usuario
frase = input("Por favor, introduce una frase: ").lower()

# Inicializamos el contador
contador_vocales = Counter()

# Recorremos cada letra de la frase
for letra in frase:
    if letra in vocales:
        contador_vocales[letra] += 1

# Mostramos resultados
total_vocales = sum(contador_vocales.values())
print(f"\nSe han encontrado {total_vocales} vocales en total.")

for vocal, cantidad in contador_vocales.items():
    print(f"\nLa vocal '{vocal}' aparece {cantidad} veces.")