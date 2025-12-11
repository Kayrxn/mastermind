import random
from src.cruce import cruzar_padres
from src.mutacion import mutar
from src.constantes import tamanio_poblacion

def crear_nueva_generacion(padres):
    """Paso 7: Población de la siguiente generación."""
    nueva_poblacion = []
    usados = []

    while len(nueva_poblacion) < tamanio_poblacion:
        padre1 = random.choice(padres)
        while padre1 in usados and len(usados) < len(padres):
            padre1 = random.choice(padres)
        usados.append(padre1)

        padre2 = random.choice(padres)
        while (padre2 == padre1 or padre2 in usados) and len(usados) < len(padres):
            padre2 = random.choice(padres)
        usados.append(padre2)

        hijo1, hijo2 = cruzar_padres(padre1, padre2)
        hijo1 = mutar(hijo1)
        hijo2 = mutar(hijo2)

        nueva_poblacion.append(hijo1)
        nueva_poblacion.append(hijo2)

    return nueva_poblacion[:tamanio_poblacion]
