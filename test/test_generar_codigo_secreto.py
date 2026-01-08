from logica.generar_codigo_secreto import generar_codigo
from logica.constantes import COLORES, LONGITUD_CODIGO

def test_generar_codigo_valido():
    codigo = generar_codigo()
    assert len(codigo) == LONGITUD_CODIGO
    for color in codigo:
        assert color in COLORES
