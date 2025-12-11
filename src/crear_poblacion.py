import random
from src.constantes import colores, longitud_codigo, tamanio_poblacion

def crear_poblacion():
    """Paso 3: Crea la población inicial."""
    poblacion = []
    for _ in range(tamanio_poblacion):
        individuo = []
        for _ in range(longitud_codigo):
            individuo.append(random.choice(colores))
        poblacion.append(individuo)
    return poblacion
