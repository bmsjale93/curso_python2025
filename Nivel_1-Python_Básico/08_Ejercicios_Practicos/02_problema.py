# Escribir un Programa que Determine si un Número es Primo

# Consejos
# Pide al usuario un número entero mayor que 1 e indica si es primo o no.

# Requisitos
# Un número es primo si solo es divisible por 1 y por sí mismo.
# Asegúrate de manejar valores negativos o inválidos.
# Usa una función es_primo(n) que devuelva True o False.

# Consejos
# Un buen enfoque es usar un bucle for que recorra desde 2 hasta n - 1.
# Puedes optimizar el código usando range(2, int(n**0.5)+1).
# Usa return False tan pronto como encuentres un divisor.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        numero = int(input("Introduce un número entero mayor que 1: "))
        if numero <= 1:
            print("El número debe ser mayor a 1.")
        else:
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__=="__main__":
    main()