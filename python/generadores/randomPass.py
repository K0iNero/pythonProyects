# Programa que genera contraseñas aleatorias configuradas por el usuario
import string
import random

print("Bienvenido. Especifica la configuración de su contraseña: ")
try:
    longitud = int(input("¿Cuantos caráteres quieres que tenga tu contraseña (longitud)? (número): "))
    minusculas = str(input("¿Quieres minúsculas en tu contraseña? (si/no): ")).strip().lower() == 'si'
    mayusculas = str(input("¿Quieres mayúsculas en tu contraseña? (si/no): ")).strip().lower() == 'si'
    caractEspec = str(input("¿Quieres carácteres especiales en tu contraseña? (si/no): ")).strip().lower() == 'si'
    numeros = str(input("¿Quieres números en tu contraseña? (si/no): ")).strip().lower() == 'si'
except ValueError:
    print("Introduce un carácter válido")

# Lista con la cadena de carácteres seleccionados:
opciones = []
if minusculas:
    opciones.extend(string.ascii_lowercase)
if mayusculas:
    opciones.extend(string.ascii_uppercase)
if caractEspec:
    opciones.extend(string.punctuation)
if numeros:
    opciones.extend(string.digits)

password = ''

# Asegurara de que al menos hay una opción
if not opciones:
    print("Debes seleccionar al menos un tipo de carácter.")
else:
    # Generar la contraseña
    password = ''.join(random.choice(opciones) for _ in range(longitud))
    print("Tu contraseña generada es:", password)
                
