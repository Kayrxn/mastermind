#generar codigo secreto

import random
from src.constantes import COLORES, LONGITUD_CODIGO

def generar_codigo():

    #Paso 2: generar código secreto aleatorio.
    codigo = []
    for _ in range(LONGITUD_CODIGO): #4 veces
        codigo.append(random.choice(COLORES)) #añade a codigo 4 colores aleatorios de la constante COLORES
    return codigo
