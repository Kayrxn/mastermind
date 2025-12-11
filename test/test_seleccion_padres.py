from src.seleccion_padres import seleccionar_padres
from src.constantes import tamanio_poblacion, colores
import random

def test_selecciona_80_por_ciento_unicos():
    # Crear población variada aleatoriamente
    poblacion = []
    for _ in range(tamanio_poblacion):
        individuo = random.sample(colores, 4)  # 4 colores distintos por individuo
        poblacion.append(individuo)
    
    codigo = random.sample(colores, 4)  # Código secreto aleatorio
    padres = seleccionar_padres(poblacion, codigo)
    
    # Comprobaciones
    assert len(padres) == int(tamanio_poblacion * 0.8)  # 80% de la población
    # No hay padres repetidos
    assert len(padres) == len(set(tuple(p) for p in padres))
