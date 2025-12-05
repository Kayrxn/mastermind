import random
from src.constantes import colores, longitud_codigo

def generar_codigo():
    return [random.choice(colores) for _ in range(longitud_codigo)]  #escoge un color aleatorio de los disponibles, y lo mete en una lista (x4)
