def calcular_fitness(individuo, codigo_secreto):
    """Paso 4: Mide la aptitud (fitness) de cada individuo."""
    negros = 0
    blancos = 0
    secreto_temp = codigo_secreto.copy()
    intento_temp = individuo.copy()

    for i in range(len(individuo)):
        if intento_temp[i] == secreto_temp[i]:
            negros += 1
            secreto_temp[i] = None
            intento_temp[i] = None

    for i in range(len(individuo)):
        if intento_temp[i] is not None and intento_temp[i] in secreto_temp:
            blancos += 1
            secreto_temp[secreto_temp.index(intento_temp[i])] = None

    return negros * 2 + blancos, negros, blancos

