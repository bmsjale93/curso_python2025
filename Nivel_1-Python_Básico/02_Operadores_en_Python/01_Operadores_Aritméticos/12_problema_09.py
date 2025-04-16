# Escribe un programa que convierta una cantidad de minutos en horas y minutos.

# Tenemos una cantidad de minutos X
x = 350

# Para calcular las horas, dividimos esta cantidad entre 60
horas = x // 60

# Para obtener los minutos restantes, podemos utilizar el módulo
minutos = x % 60

# Imprimimos el resultado
print(f"Si tenemos {x} minutos, correspondería a {horas} horas y {minutos} minutos.")