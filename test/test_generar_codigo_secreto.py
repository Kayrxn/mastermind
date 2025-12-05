from src.generar_codigo_secreto import generar_codigo
from src.constantes import colores, longitud_codigo

def test_generar_codigo_valido():
    codigo = generar_codigo()
    assert len(codigo) == longitud_codigo
    assert all(color in colores for color in codigo)