#mutacion

import random
from src.constantes import COLORES, PROB_MUTACION

def mutar(individuo):
    #Paso 6 (parte 2): Aplica mutación aleatoria.

    nuevo = individuo.copy()
    if random.random() < PROB_MUTACION:    #se lanza un número aleatorio entre 0 y 1, y si es menor que PROB_MUTACION (0.10)...
        indice = random.randint(0, len(individuo) - 1)  #elige un índice aleatorio del individuo
        nuevo[indice] = random.choice(COLORES)  #y cambia el color en ese índice por uno aleatorio de COLORES
    return nuevo
