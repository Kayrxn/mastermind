from src.seleccion import seleccion_individuos

def test_seleccionar_individuo_mitad_poblacion():
    poblacion = [
        ["rojo", "verde", "azul", "amarillo"],
        ["rojo", "rojo", "rojo", "rojo"],
        ["verde", "verde", "verde", "verde"],
        ["azul", "azul", "azul", "azul"],
    ]
    codigo = ["rojo", "verde", "azul", "amarillo"]
    individuos_seleccionados = seleccion_individuos(poblacion, codigo)
    assert len(individuos_seleccionados) == len(poblacion) // 2

def test_seleccionar_individuo_identicos():

    poblacion = [
        ["rojo", "rojo", "rojo", "rojo"],
        ["rojo", "rojo", "rojo", "rojo"],
        ["rojo", "rojo", "rojo", "rojo"],
        ["rojo", "rojo", "rojo", "rojo"],
    ]
    codigo = ["rojo", "rojo", "rojo", "rojo"]
    individuos_seleccionados = seleccion_individuos(poblacion, codigo)

    assert len(individuos_seleccionados) == len(poblacion) // 2

    