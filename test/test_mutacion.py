from logica.mutacion import mutar

def test_mutacion_mismo_tamano():
    ind = ["rojo", "verde", "azul", "amarillo"]
    resultado = mutar(ind)
    assert len(resultado) == len(ind)
