import random
from logica.constantes import COLORES, PROB_MUTACION

def mutar(individuo):
    #Paso 6 (parte 2): Aplica mutación aleatoria.

    if random.random() < PROB_MUTACION:    #se lanza un número aleatorio entre 0 y 1, y si es menor que PROB_MUTACION...
        indice = random.randint(0, len(individuo) - 1)  #elige un índice aleatorio del individuo
        individuo[indice] = random.choice(COLORES)  #y cambia el color en ese índice por uno aleatorio de COLORES
    return individuo
