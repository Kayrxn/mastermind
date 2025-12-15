from src.fitness import calcular_fitness
from src.constantes import TAMANIO_POBLACION

def seleccionar_padres(poblacion, codigo_secreto):
    #Paso 5: Selecciona el 80% superior por fitness, sin repetir padres.

    resultados = []  #guardará tuplas (individuo, valor_fitness)
    for individuo in poblacion:
        fit, _, _ = calcular_fitness(individuo, codigo_secreto)
        resultados.append([individuo, fit])

    #ordenar manualmente por fitness
    n = len(resultados)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if resultados[j][1] < resultados[j + 1][1]:
                temp = resultados[j]
                resultados[j] = resultados[j + 1]
                resultados[j + 1] = temp

    numero_padres = int(TAMANIO_POBLACION * 0.8)
    padres = []
    usados = []

    indice = 0
    while len(padres) < numero_padres and indice < len(resultados):
        candidato = resultados[indice][0]
        if candidato not in usados:
            padres.append(candidato)
            usados.append(candidato)
        indice = indice + 1

    return padres
