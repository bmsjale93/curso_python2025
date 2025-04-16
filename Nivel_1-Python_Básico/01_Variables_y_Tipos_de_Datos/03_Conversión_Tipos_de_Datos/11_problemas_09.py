# Escribe un programa que convierta la tupla("Lunes", "Martes", "Miércoles") 
# en una lista y agregue "Jueves".

tupla = ("Lunes", "Martes", "Miércoles")
lista = list(tupla)
lista.append("Jueves")
print(lista)
print(type(lista))