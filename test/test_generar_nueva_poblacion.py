import pytest
from src.generar_nueva_poblacion import generar_nueva_poblacion
from src.constantes import tamanio_poblacion, colores


def test_generar_nueva_poblacion_tamano():
    padres = [
        ["rojo", "verde", "azul", "amarillo"],
        ["blanco", "negro", "azul", "rojo"],
        ["verde", "blanco", "amarillo", "negro"],
        ["azul", "rojo", "verde", "blanco"]
    ]
    nueva = generar_nueva_poblacion(padres)
    assert len(nueva) == tamanio_poblacion


def test_generar_nueva_poblacion_colores_validos():
    padres = [
        ["rojo", "verde", "azul", "amarillo"],
        ["blanco", "negro", "azul", "rojo"],
        ["verde", "blanco", "amarillo", "negro"],
        ["azul", "rojo", "verde", "blanco"]
    ]
    nueva = generar_nueva_poblacion(padres)
    for ind in nueva:
        for color in ind:
            assert color in colores


def test_generar_nueva_poblacion_individuos_distintos():
    padres = [
        ["rojo", "verde", "azul", "amarillo"],
        ["blanco", "negro", "azul", "rojo"]
    ]
    nueva = generar_nueva_poblacion(padres)
    nueva_set = set(tuple(ind) for ind in nueva)
    assert len(nueva_set) > 1


def test_generar_nueva_poblacion_diferente_de_padres():
    padres = [
        ["rojo", "rojo", "rojo", "rojo"],
        ["verde", "verde", "verde", "verde"]
    ]
    nueva = generar_nueva_poblacion(padres)
    dif = any(ind not in padres for ind in nueva)
    assert dif
