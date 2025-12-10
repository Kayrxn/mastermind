import random
from src.constantes import tamanio_poblacion
from src.cruce import cruce_padres
from src.mutacion import mutacion

def generar_nueva_poblacion(padres):
    nueva_poblacion = []

    while len(nueva_poblacion) < tamanio_poblacion:

        p1, p2 = random.sample(padres, 2)
        h1, h2 = cruce_padres(p1, p2)
        nueva_poblacion.extend([mutacion(h1), mutacion(h2)])

    return nueva_poblacion[:tamanio_poblacion]

