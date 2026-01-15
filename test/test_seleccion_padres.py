import pytest
from logica.seleccion_padres import seleccionar_padres
from logica.constantes import TAMANIO_POBLACION, COLORES
import random

@pytest.mark.seleccion_50_por_ciento_unicos
def test_selecciona_50_por_ciento_unicos():
    #crear población variada aleatoriamente
    poblacion = []
    for _ in range(TAMANIO_POBLACION):
        individuo = random.sample(COLORES, 4)  #4 colores distintos por individuo
        poblacion.append(individuo)
    
    codigo = random.sample(COLORES, 4)  #código secreto aleatorio
    padres = seleccionar_padres(poblacion, codigo)
    
    # Comprobaciones
    assert len(padres) == int(TAMANIO_POBLACION * 0.5)  #50% de la población
