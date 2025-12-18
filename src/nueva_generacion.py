#nueva generacion

import random
from src.cruce import cruzar_padres
from src.mutacion import mutar
from src.constantes import TAMANIO_POBLACION
from src.fitness import calcular_fitness

def crear_nueva_generacion(padres, codigo_secreto=None):

    #Paso 7: Población de la siguiente generación.
    nueva_poblacion = []
    usados = []

    while len(nueva_poblacion) < TAMANIO_POBLACION: #mientras no se llene la nueva población

        padre1 = random.choice(padres) #elegir dos padres aleatoriamente
        while padre1 in usados and len(usados) < len(padres): #mientras padre1 sea igual a 2 (o esté ya usado), y la longitud de usados sea menor a longitud de padres 
            padre1 = random.choice(padres) #padre1 será un padre aleatorio
        usados.append(padre1)

        padre2 = random.choice(padres) #elegir segundo padre aleatoriamente
        while (padre2 == padre1 or padre2 in usados) and len(usados) < len(padres): #mientras padre2 sea igual a 1 (o esté ya usado), y la longitud de usados sea menor a longitud de padres 
            padre2 = random.choice(padres) #padre2 será un padre aleatorio
        usados.append(padre2)

        hijo1, hijo2 = cruzar_padres(padre1, padre2) #cruzar padres para crear hijos
        hijo1 = mutar(hijo1)
        hijo2 = mutar(hijo2)

        nueva_poblacion.append(hijo1)
        nueva_poblacion.append(hijo2)

    #Si se proporcionó el código secreto, ordenar por fitness descendente
    if codigo_secreto is not None:
        nueva_poblacion.sort(key=lambda x: calcular_fitness(x, codigo_secreto)[0], reverse=True)

    return nueva_poblacion[:TAMANIO_POBLACION]
