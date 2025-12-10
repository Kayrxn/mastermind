import random
from src.constantes import longitud_codigo

def cruce_padres (padre1, padre2):

    codigo_parentesco = random.randint(1, longitud_codigo -1)

    hijo1, hijo2 = padre1[:codigo_parentesco] + padre2[codigo_parentesco:], padre2[:codigo_parentesco] + padre1[codigo_parentesco:]
    
    return hijo1, hijo2
