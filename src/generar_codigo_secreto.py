import random

colores = ["rojo", "verde", "azul", "amarillo", "blanco", "negro", "rosa", "marrón"]
longitud_codigo = 4

def generar_codigo_secreto():
    codigo = []
    for _ in range(longitud_codigo):
        color_aleatorio = random.choice(colores)
        codigo.append(color_aleatorio)
    return codigo