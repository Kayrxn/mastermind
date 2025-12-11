import random
from src.constantes import tamanio_poblacion
from src.cruce import cruce_padres
from src.mutacion import mutacion
from seleccion import seleccion_individuos

def generar_nueva_poblacion(padres):
    nueva_poblacion = []
    padres_disponibles = padres.copy()

    while len(padres_disponibles) >= 2 and len(nueva_poblacion) < tamanio_poblacion:
        padre_a, padre_b = random.sample(padres_disponibles, 2)
        padres_disponibles.remove(padre_a)
        padres_disponibles.remove(padre_b)
        if padres_disponibles == []:
            padres_disponibles = padres.copy()
        

        hijo_a, hijo_b = cruce_padres(padre_a, padre_b)
        hijo_a = mutacion(hijo_a)
        hijo_b = mutacion(hijo_b)

        # Evitar que hijos sean exactamente iguales a padres
        if hijo_a in padres:
            hijo_a = mutacion(hijo_a)
        if hijo_b in padres:
            hijo_b = mutacion(hijo_b)

        nueva_poblacion.append(hijo_a)
        if len(nueva_poblacion) < tamanio_poblacion:
            nueva_poblacion.append(hijo_b)

    return nueva_poblacion
