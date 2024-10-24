# Programa: Juego del ahorcado utilizando random - Israel

import random

# Lista de palabras predefinidas
palabras = ["python", "javascript", "hangman", "challenge", "programming"]

# Seleccionar una palabra al azar
palabra = random.choice(palabras).lower()  # Asegurarnos de que esté en minúsculas para la comparación

# Inicializar variables del juego
intentos_maximos = 6
intentos = 0
letras_adivinadas = set()  # Para no repetir las letras adivinadas
letras_correctas = set(palabra)  # Todas las letras correctas de la palabra

# Representación del progreso del jugador
progreso_palabra = ['_' for _ in palabra]

# Definición para mostrar el progreso
def mostrar_ahorcado(intentos):
    etapas = [
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """
    ]
    print(etapas[intentos])

# Bucle del juego
while intentos < intentos_maximos and set(progreso_palabra) != letras_correctas:
    print("\nPalabra:", ' '.join(progreso_palabra))
    print(f"Intentos restantes: {intentos_maximos - intentos}")
    mostrar_ahorcado(intentos)

    # Obtener la entrada del usuario
    letra = input("Adivina una letra: ").lower()

    # Validar la letra ingresada
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor ingresa una sola letra válida.")
        continue

    # Verificar si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra.")
        continue

    # Añadir la letra a las letras adivinadas
    letras_adivinadas.add(letra)

    # Comprobar si la letra está en la palabra
    if letra in letras_correctas:
        for indice, caracter in enumerate(palabra):
            if caracter == letra:
                progreso_palabra[indice] = letra
    else:
        intentos += 1  # Incrementar los intentos solo si la letra no está
    
# Resultados finales
mostrar_ahorcado(intentos)
if set(progreso_palabra) == letras_correctas:
    print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
else:
    print(f"Lo siento, te has quedado sin intentos. La palabra era: {palabra}")