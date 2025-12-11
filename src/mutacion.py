import random
from src.constantes import colores, prob_mutacion

def mutar(individuo):
    """Paso 6 (parte 2): Aplica mutación aleatoria."""
    nuevo = individuo.copy()
    if random.random() < prob_mutacion:
        indice = random.randint(0, len(individuo) - 1)
        nuevo[indice] = random.choice(colores)
    return nuevo
