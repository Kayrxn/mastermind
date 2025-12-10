import random
from src.constantes import tamanio_poblacion, colores, longitud_codigo

def crear_poblacion():
    return [[random.choice(colores) for _ in range(longitud_codigo)] for _ in range(tamanio_poblacion)]
