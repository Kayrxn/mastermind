import random
from src.constantes import COLORES, PROB_MUTACION

def mutar(individuo):
    """Paso 6 (parte 2): Aplica mutación aleatoria."""
    nuevo = individuo.copy()
    if random.random() < PROB_MUTACION:
        indice = random.randint(0, len(individuo) - 1)
        nuevo[indice] = random.choice(COLORES)
    return nuevo
