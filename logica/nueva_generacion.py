import random
from logica.cruce import cruzar_padres
from logica.mutacion import mutar
from logica.constantes import TAMANIO_POBLACION

def crear_nueva_generacion(padres):

    #Paso 7: Población de la siguiente generación.
    nueva_poblacion = []
    #nueva_poblacion = padres.copy() #añadir a los mejores padres a la anterior generacion
    usados = []

    while len(nueva_poblacion) < TAMANIO_POBLACION: #mientras no se llene la nueva población

        padre1 = random.choice(padres) #escoge un padre1 aleatorio
        while padre1 in usados and len(usados) < len(padres): #si ese padre1 es igual a padre2 o ya está usado, y MIENTRAS [usados] aún no está lleno...
            padre1 = random.choice(padres) #haces reroll del padre1
        usados.append(padre1)

        padre2 = random.choice(padres) #escoge un padre2 aleatorio
        while (padre2 == padre1 or padre2 in usados) and len(usados) < len(padres): #si ese padre2 es igual a padre1 o ya está usado, y MIENTRAS [usados] aún no está lleno...
            padre2 = random.choice(padres) #haces reroll del padre2
        usados.append(padre2)

        hijo1, hijo2 = cruzar_padres(padre1, padre2) #cruzar padres para crear hijos
        hijo1 = mutar(hijo1)
        hijo2 = mutar(hijo2)

        nueva_poblacion.append(hijo1)
        nueva_poblacion.append(hijo2)

    return nueva_poblacion