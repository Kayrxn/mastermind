from src.fitness import calcular_fitness

def test_calculo_fitness_correcto():
    codigo = ["rojo", "verde", "azul", "amarillo"]
    intento = ["rojo", "azul", "azul", "negro"]
    puntos, negros, blancos = calcular_fitness(intento, codigo)
    assert negros == 2       # coincidencias exactas: posición 0 y 2
    assert blancos == 0      # coincidencias de color en otra posición: ninguna
    assert puntos == 4       # fitness = 2*negros + blancos = 4
