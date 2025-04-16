# Escribe un for que imprima los números del 1 al 10, saltándose el número 5 usando continue .

for i in range(1, 11):
    if i == 5:
        continue
    print(i)