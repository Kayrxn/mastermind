import random
from src.fitness import fitness

def seleccion_individuos (poblacion, codigo_secreto):

    individuos_seleccionados = []
    
    for _ in range(len(poblacion) // 2):
        padre_a, padre_b = random.sample(poblacion, 2)
        
        if fitness(padre_a, codigo_secreto) > fitness(padre_b,codigo_secreto):
            ganador = padre_a
        
        else:
            ganador = padre_b
        
        individuos_seleccionados.append(ganador)
        
    return individuos_seleccionados