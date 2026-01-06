def cruzar_padres(padre1, padre2):
    #Paso 6: Cruza dos padres.

    hijo1 = padre1[:2] + padre2[2:] 
    hijo2 = padre2[:2] + padre1[2:]
    return hijo1, hijo2
