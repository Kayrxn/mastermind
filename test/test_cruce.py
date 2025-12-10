from src.cruce import cruce

def test_cruce_comprobar_longitud():
    p1 = ["rojo", "verde", "azul", "amarillo"]
    p2 = ["blanco", "negro", "negro", "verde"]
    h1, h2 = cruce(p1, p2)
    assert len(h1) == len(p1)
    assert len(h2) == len(p2)

def test_cruce_hijos_solo_colores_de_padres():
    p1 = ["rojo", "verde", "azul", "amarillo"]
    p2 = ["blanco", "negro", "negro", "verde"]
    
    h1, h2 = cruce(p1, p2)
    
    for color in h1:
        assert color in p1 + p2
    
    for color in h2:
        assert color in p1 + p2