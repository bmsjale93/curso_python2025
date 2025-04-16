# Define una función que reciba un email y lance un ValueError si no contiene "@".

def comprobar_email(email):
    if "@" not in email:
        raise ValueError("\nEl email introducido no es correcto")

try:
    email = input("Por favor, introduce un email: ")
    comprobar_email(email)
    print(f"El email introducido es correcto: {email}")
except Exception as e:
    print("Se ha producido un error: ", e)