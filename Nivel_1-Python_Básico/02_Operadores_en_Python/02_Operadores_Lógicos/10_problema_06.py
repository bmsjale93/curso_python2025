# Crea un programa que solicite al usuario dos valores booleanos(a y b), 
# y muestre los resultados de a and b, a or b y not a.

# Pedimos al usuario que le de valor a las variables
a = input("Establece un valor para 'a' (True o False): ").strip().lower() == "true"
print(f"Usted ha seleccionado que a = {a}.")

b = input("Establece un valor para 'b' (True o False): ").strip().lower() == "true"
print(f"Usted ha seleccionado que b = {b}.")

# Aplicando los operadores lógicos
print("\nAplicamos los operadores lógicos:")
print("Resultado de aplicar AND: ", a and b)
print("Resultado de aplicar OR: ", a or b)
print("Resultado de aplicar NOT: ", not a)