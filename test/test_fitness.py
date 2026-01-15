import pytest
from logica.fitness import calcular_fitness

@pytest.mark.calculo_fitness_correcto
def test_calculo_fitness_correcto():
    codigo = ["rojo", "verde", "azul", "amarillo"]
    intento = ["rojo", "azul", "azul", "negro"]
    puntos, negros, blancos = calcular_fitness(intento, codigo)
    assert negros == 2   
    assert blancos == 0   
    assert puntos == 4  
