from src.crear_poblacion import crear_poblacion
from src.constantes import tamanio_poblacion, colores, longitud_codigo

def test_crear_poblacion_tamano():
    poblacion = crear_poblacion()
    assert len(poblacion) == tamanio_poblacion

def test_crear_poblacion_individuos_tamano_correcto():
    poblacion = crear_poblacion()
    for individuo in poblacion:
        assert len(individuo) == longitud_codigo

def test_crear_poblacion_colores_validos():
    poblacion = crear_poblacion()
    for individuo in poblacion:
        for color in individuo:
            assert color in colores