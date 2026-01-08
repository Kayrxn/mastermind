from logica.crear_poblacion import crear_poblacion
from logica.constantes import TAMANIO_POBLACION, LONGITUD_CODIGO

def test_tamano_poblacion():
    poblacion = crear_poblacion()
    assert len(poblacion) == TAMANIO_POBLACION
    assert all(len(ind) == LONGITUD_CODIGO for ind in poblacion)
