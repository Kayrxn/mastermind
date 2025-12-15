from src.seleccion_padres import seleccionar_padres
from src.constantes import TAMANIO_POBLACION, COLORES
import random

def test_selecciona_80_por_ciento_unicos():
    # Crear población variada aleatoriamente
    poblacion = []
    for _ in range(TAMANIO_POBLACION):
        individuo = random.sample(COLORES, 4)  # 4 colores distintos por individuo
        poblacion.append(individuo)
    
    codigo = random.sample(COLORES, 4)  # Código secreto aleatorio
    padres = seleccionar_padres(poblacion, codigo)
    
    # Comprobaciones
    assert len(padres) == int(TAMANIO_POBLACION * 0.8)  # 80% de la población
    # No hay padres repetidos
    assert len(padres) == len(set(tuple(p) for p in padres))
