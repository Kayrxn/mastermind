#selección_padres

from src.fitness import calcular_fitness
from src.constantes import TAMANIO_POBLACION

def seleccionar_padres(poblacion, codigo_secreto):
    # Paso 5: Selecciona el 50% superior por fitness, sin repetir padres.

    resultados = []  #creamos lista para los resultados [[individuo, valor_fitness],[individuo, valor_fitness], ...]
    for individuo in poblacion:
        fit, _, _ = calcular_fitness(individuo, codigo_secreto)
        resultados.append([individuo, fit])

    #Ordenar por fitness de mayor a menor
    resultados_ordenados = sorted(resultados, key=lambda intento: intento[1], reverse=True)
    #lista a ordenar, factor de ordenación, orden descendente

    numero_padres = int(TAMANIO_POBLACION * 0.5) #selecciona el 50% de la población como numero_padres
    padres = []
    usados = []

    for individuo, _ in resultados_ordenados:  #recorre los individuos en resultados_ordenados (ordenados por fitness)
        if len(padres) >= numero_padres:  #si ya se han seleccionado suficientes padres, salir del bucle
            break
        if individuo not in usados:  #si el individuo no está ya en usados (para evitar duplicados)...
            padres.append(individuo)  #añadir individuo a padres
            usados.append(individuo)  #y a usados

    return padres

