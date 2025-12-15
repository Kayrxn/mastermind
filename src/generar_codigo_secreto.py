import random
from src.constantes import COLORES, LONGITUD_CODIGO

def generar_codigo():
    codigo = []
    for _ in range(LONGITUD_CODIGO):
        codigo.append(random.choice(COLORES))
    return codigo
