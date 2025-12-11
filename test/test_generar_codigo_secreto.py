from src.generar_codigo_secreto import generar_codigo
from src.constantes import colores, longitud_codigo

def test_generar_codigo_valido():
    codigo = generar_codigo()
    assert len(codigo) == longitud_codigo
    for color in codigo:
        assert color in colores
