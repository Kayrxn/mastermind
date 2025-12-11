import random
from src.constantes import longitud_codigo

def cruzar_padres(padre1, padre2):
    """Paso 6: Cruza dos padres en un punto."""
    punto = random.randint(1, longitud_codigo - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2
