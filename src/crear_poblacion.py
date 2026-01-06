import random
from src.constantes import COLORES, LONGITUD_CODIGO, TAMANIO_POBLACION

def crear_poblacion():
    #Paso 3: Crea la población inicial.

    poblacion = []
    for _ in range(TAMANIO_POBLACION): #80 veces
        individuo = []
        for _ in range(LONGITUD_CODIGO): #sacar 4 colores aleatorios
            individuo.append(random.choice(COLORES))
        poblacion.append(individuo)
    return poblacion
