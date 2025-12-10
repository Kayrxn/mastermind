from src.ejecutar_algoritmo_genetico import ejecutar_algoritmo_genetico
from src.crear_poblacion import crear_poblacion

def test_algoritmo_funciona_basico():
    codigo_secreto = ["rojo", "verde", "azul", "amarillo"]
    poblacion = crear_poblacion()
    mejor, generaciones = ejecutar_algoritmo_genetico(codigo_secreto, poblacion, max_generaciones=5)

    #el resultado debe ser una lista (la mejor combinación)
    assert isinstance(mejor, list)
    #debe tener 4 colores
    assert len(mejor) == 4
    #el número de generaciones no debe pasarse del máximo
    assert generaciones <= 5
