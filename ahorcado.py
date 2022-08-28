import random

from list_palabras import palabras

def obtener_palabra_valida(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra

print(obtener_palabra_valida())
