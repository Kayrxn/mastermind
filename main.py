from src.constantes import MAX_GENERACION
from src.generar_codigo_secreto import generar_codigo
from src.crear_poblacion import crear_poblacion
from src.fitness import calcular_fitness
from src.seleccion_padres import seleccionar_padres
from src.nueva_generacion import crear_nueva_generacion

def main():

    codigo_secreto = generar_codigo()
    print(f"Código secreto: {codigo_secreto}\n")

    # 3. Create initial population
    poblacion = crear_poblacion()

    # Bucle principal de generaciones
    generacion = 1
    while generacion <= MAX_GENERACION:
        # 4. Measure fitness of individuals
        mejor = poblacion[0]
        mejor_fitness, negros, blancos = calcular_fitness(mejor, codigo_secreto)

        for individuo in poblacion:
            fit, n, b = calcular_fitness(individuo, codigo_secreto)
            if fit > mejor_fitness:
                mejor = individuo
                mejor_fitness = fit
                negros = n
                blancos = b

        # Mostrar intento
        visual = "●" * negros + "○" * blancos + " " * (len(codigo_secreto) - negros - blancos)
        print("Intento", generacion, ":", mejor, visual)

        # Comprobar si adivinó el código
        if mejor == codigo_secreto:
            print("\n¡La máquina adivinó el código en la generación", generacion, "!")
            return

        # 5. Select parents
        padres = seleccionar_padres(poblacion, codigo_secreto)

        # 6–7. Reproduce offspring & populate next generation
        poblacion = crear_nueva_generacion(padres, codigo_secreto)  # Pasar codigo_secreto

        generacion = generacion + 1

    print("\nNo se adivinó el código dentro del límite de generaciones.")

if __name__ == "__main__":
    main()

