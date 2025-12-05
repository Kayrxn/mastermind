from src.generar_codigo_secreto import *

def test_generar_codigo_secreto():
    assert len(generar_codigo_secreto()) == longitud_codigo
    assert all(color in colores for color in generar_codigo_secreto())

print("Todas las pruebas pasaron correctamente.") 