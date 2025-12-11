from src.crear_poblacion import crear_poblacion
from src.constantes import tamanio_poblacion, longitud_codigo

def test_tamano_poblacion():
    poblacion = crear_poblacion()
    assert len(poblacion) == tamanio_poblacion
    assert all(len(ind) == longitud_codigo for ind in poblacion)
