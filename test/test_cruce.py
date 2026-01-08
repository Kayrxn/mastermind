from logica.cruce import cruzar_padres

def test_cruce_dos_hijos_mismo_tamano():
    p1 = ["rojo", "verde", "azul", "amarillo"]
    p2 = ["negro", "blanco", "blanco", "verde"]
    h1, h2 = cruzar_padres(p1, p2)
    assert len(h1) == 4 and len(h2) == 4
