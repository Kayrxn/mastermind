import random
from src.fitness import fitness

def seleccion_individuos (poblacion, codigo_secreto):

    individuos_seleccionados = []
    
    for _ in range(len(poblacion) // 2):
        primer_individuo, segundo_individuo = random.sample(poblacion, 2)
        
        if fitness(primer_individuo, codigo_secreto) > fitness(segundo_individuo,codigo_secreto):
            ganador = primer_individuo
        
        else:
            ganador = segundo_individuo
        
        individuos_seleccionados.append(ganador)
        
    return individuos_seleccionados