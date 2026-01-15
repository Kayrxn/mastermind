import pytest
from logica.mutacion import mutar

@pytest.mark.mutacion_mismo_tamano
def test_mutacion_mismo_tamano():
    ind = ["rojo", "verde", "azul", "amarillo"]
    resultado = mutar(ind)
    assert len(resultado) == len(ind)
