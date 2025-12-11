import random
from src.constantes import colores, longitud_codigo

def generar_codigo():
    codigo = []
    for _ in range(longitud_codigo):
        codigo.append(random.choice(colores))
    return codigo
