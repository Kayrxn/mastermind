from src.fitness import fitness  


def test_todo_correcto():
    codigo_secreto = ["rojo", "verde", "azul", "amarillo"]
    individuo = ["rojo", "verde", "azul", "amarillo"]
    assert fitness(individuo, codigo_secreto) == 8


def test_aciertos_mixtos():
    codigo_secreto = ["rojo", "verde", "azul", "amarillo"]
    individuo = ["rojo", "azul", "verde", "negro"]
    assert fitness(individuo, codigo_secreto) == 4


def test_ningun_acierto():
    codigo_secreto = ["rojo", "verde", "azul", "amarillo"]
    individuo = ["blanco", "negro", "negro", "blanco"]
    assert fitness(individuo, codigo_secreto) == 0
