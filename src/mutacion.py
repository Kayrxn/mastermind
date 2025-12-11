import random
from src.constantes import colores, prob_mutacion

def mutacion(individuo):
    nuevo = individuo.copy()

    if random.random() < prob_mutacion:

        indice = random.randint(0, len(individuo) - 1)
        color_actual = nuevo[indice]

        # crear lista de colores posibles excluyendo el actual
        colores_posibles = []
        for color in colores:
            if color != color_actual:
                colores_posibles.append(color)

        # elegir uno distinto al actual
        nuevo[indice] = random.choice(colores_posibles)

    return nuevo
