# Cuantos puntos ganas si aciertas posicion+color o sólo color

def fitness(individuo, codigo_secreto):
    puntos = 0

    #copias para no cambiar los originales
    secreto_copy = codigo_secreto.copy()
    individuo_copy = individuo.copy()

    #comprueba si acierta posicion+color
    for i in range(len(individuo)):                 
        if individuo[i] == codigo_secreto[i]:    #si es lo mismo en la misma posición
            puntos += 2                          #gana 2 puntos
            
            secreto_copy[i] = None     #te cargas (reemplazas por None porque ya se usó) el color en el código secreto
            individuo_copy[i] = None   #y también en el individuo

    #comprueba si acierta color
    for i in range(len(individuo_copy)):
        color_actual = individuo_copy[i]        #guardamos el color actual
        if color_actual is not None:            #ignoramos los None que vienen de arriba (acertados)
            if color_actual in secreto_copy:    #si el color está en /alguna/ posición del código secreto
                puntos += 1                     #ganas 1 punto

                index = secreto_copy.index(color_actual)   #obtén la posición del color actual en el códgigo secreto
                secreto_copy[index] = None                 #y esa posición, te la cargas (reemplazas por None porque ya se usó)

    return puntos
