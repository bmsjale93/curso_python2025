# Crear un Conversor de Temperatura entre Celsius y Fahrenheit

# Descripción
# El programa debe permitir convertir de Celsius a Fahrenheit y viceversa, según la elección del usuario.

# Requisitos
# Fórmulas:
# Celsius → Fahrenheit: F = C * 9/5 + 32
# Fahrenheit → Celsius: C = (F - 32) * 5/9
# Validar entradas numéricas.
# Permitir elegir el tipo de conversión.

# Consejos
# Usa funciones c_to_f() y f_to_c() para mantener el código organizado.
# Asegúrate de manejar entradas no válidas con try -except .
# Puedes usar un menú sencillo para seleccionar el tipo de conversión.

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Conversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        try:
            celsius = float(input("Introduce la temperatura en Celsius: "))
            resultado = c_to_f(celsius)
            print(f"{celsius}°C son {resultado:.2f}°F")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    elif opcion == "2":
        try:
            fahrenheit = float(
                input("Introduce la temperatura en Fahrenheit: "))
            resultado = f_to_c(fahrenheit)
            print(f"{fahrenheit}°F son {resultado:.2f}°C")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    else:
        print("Opción no válida. Debes elegir 1 o 2.")


if __name__ == "__main__":
    main()