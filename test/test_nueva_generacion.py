# test_nueva_generacion_colores.py
from src.nueva_generacion import crear_nueva_generacion
from src.constantes import tamanio_poblacion, colores

def test_nueva_generacion_colores():
    padres = [
        ["rojo", "verde", "azul", "amarillo"],
        ["blanco", "negro", "rojo", "verde"],
        ["azul", "azul", "blanco", "negro"],
        ["amarillo", "rojo", "verde", "blanco"]
    ]
    
    nueva = crear_nueva_generacion(padres)
    
    # 1. Tamaño correcto
    assert len(nueva) == tamanio_poblacion
    
    # 2. Todos son listas
    for ind in nueva:
        assert isinstance(ind, list)
    
    # 3. Todos los colores están permitidos
    for ind in nueva:
        for color in ind:
            assert color in colores
