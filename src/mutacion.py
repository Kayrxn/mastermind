import random
from src.constantes import colores, prob_mutacion

def mutacion(individuo):
    nuevo = individuo.copy()                                #copiamos el individuo para no modificar el original

    if random.random() < prob_mutacion:                     #si se cumple la probabilidad de mutacion
        indice = random.randint(0, len(individuo) - 1)      #elegimos uno de los índices del individuo, desde 0 hasta 3 aleatoriamente (longitud es 4, menos uno porque ya contamos desde 0)
        nuevo[indice] = random.choice(colores)              #cambiamos el color en ese indice por uno aleatorio

    return nuevo
