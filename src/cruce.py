#cruce

import random
from src.constantes import LONGITUD_CODIGO

def cruzar_padres(padre1, padre2):
    #Paso 6: Cruza dos padres.

    punto = random.randint(1, LONGITUD_CODIGO - 1) #punto de cruce entre 1 y 2
    hijo1 = padre1[:punto] + padre2[punto:] 
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2
