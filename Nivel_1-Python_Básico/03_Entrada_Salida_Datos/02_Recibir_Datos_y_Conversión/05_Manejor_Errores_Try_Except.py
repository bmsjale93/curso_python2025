# Manejo de Errores con try -except
# Si el usuario ingresa un valor incorrecto(como texto en lugar de un número), 
# se generará un error.
# Para evitarlo, se usa try -except:

try:
    edad = int(input("Ingresa tu edad: "))
    print(f"En 5 años tendrás {edad + 5} años.")
except ValueError:
    print("Error: Ingresa un número válido.")