from src.fitness import fitness
from src.seleccion import seleccion
from src.crear_poblacion import crear_poblacion
from src.generar_nueva_poblacion import generar_nueva_poblacion

def ejecutar_algoritmo_genetico(codigo_secreto, poblacion=None, max_generaciones=50):

    #si no se pasa una población inicial, la creamos
    if poblacion is None:
        poblacion = crear_poblacion()

    #bucle principal del algoritmo genético
    for generacion in range(1, max_generaciones + 1):

        #calcular la aptitud de cada individuo
        puntajes = []
        for individuo in poblacion:
            puntaje = fitness(individuo, codigo_secreto)
            puntajes.append((individuo, puntaje))

        #buscar el mejor individuo de la generación
        mejor_individuo, mejor_puntaje = puntajes[0]
        for ind, score in puntajes:
            if score > mejor_puntaje:
                mejor_individuo = ind
                mejor_puntaje = score

        #si el mejor coincide con el código secreto, terminamos
        if mejor_individuo == codigo_secreto:
            return mejor_individuo, generacion

        #seleccionar padres y generar la nueva población
        padres = seleccion(poblacion, codigo_secreto)
        nueva_poblacion = generar_nueva_poblacion(padres)
        poblacion = nueva_poblacion

    #si no se adivina, devolver el mejor encontrado
    #repetimos la búsqueda final 
    mejor_individuo, mejor_puntaje = puntajes[0]
    for ind, score in puntajes:
        if score > mejor_puntaje:
            mejor_individuo = ind
            mejor_puntaje = score

    return mejor_individuo, max_generaciones
