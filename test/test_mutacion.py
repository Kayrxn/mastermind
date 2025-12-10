from src.mutacion import mutacion

def test_mutacion_devuelve_lista_mismo_tamano():
    ind = ["rojo", "verde", "azul", "amarillo"]
    mutado = mutacion(ind)
    assert len(mutado) == len(ind)