import random
import string

from list_palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(lista_palabras):
    palabra = random.choice(lista_palabras)

    while "_" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():
    print("""
     +====================================+
     | ¡Bienvenido al juego del ahorcado! |
     +====================================+ 
     """
    )
    palabra = obtener_palabra_valida(list_palabras)


    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras:
              {' '.join(letras_por_adivinar)}")

        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        #Muestra el estado actual del ahorcado
        else '_' for letra in palabra]
        # Mostrar las letras separadas por un espacio
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {''.join(palabra_lista)})

    
