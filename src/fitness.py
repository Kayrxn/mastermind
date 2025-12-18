#fitness

def calcular_fitness(individuo, codigo_secreto):
    #Paso 4: Mide la aptitud (fitness) de cada individuo.

    negros = 0  #contadores para pines negros
    blancos = 0  #contadores para pines blancos
    secreto = codigo_secreto.copy()
    intento = individuo.copy()

    for i in range(len(individuo)):  #4 veces
        if intento[i] == secreto[i]:  #si coincide exactamente
            negros += 1  #incrementar negros
            secreto[i] = None  #marcar como usado
            intento[i] = None  #marcar como usado

    for i in range(len(individuo)):  #recorrer de nuevo
        if intento[i] is not None and intento[i] in secreto:  #si existe el color
            blancos += 1  #incrementar blancos
            secreto[secreto.index(intento[i])] = None  #marcar como usado

    return negros * 2 + blancos, negros, blancos  #retornar fitness y conteos


# retorna "negros * 2 + blancos" que es el valor fitness, 
# y luego la cantidad de pines negros y blancos independientes