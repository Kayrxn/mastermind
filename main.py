from logica.constantes import MAX_GENERACION, COLORES
from logica.generar_codigo_secreto import generar_codigo
from logica.crear_poblacion import crear_poblacion
from logica.fitness import calcular_fitness
from logica.seleccion_padres import seleccionar_padres
from logica.nueva_generacion import crear_nueva_generacion

# -------------------- IMPORTAR FUNCIONES DE MATPLOTLIB --------------------

from presentacion.graficos import graficar_tablero, graficar_barras_fitness_por_generacion_y_color
import matplotlib
matplotlib.use("TkAgg")  # Forzar backend que abre ventana de gráficos

def fitness_por_color(poblacion, codigo_secreto):
    colores = COLORES
    conteo = {color: [] for color in colores}

    for individuo in poblacion:
        fit, _, _ = calcular_fitness(individuo, codigo_secreto)
        for color in set(individuo):
            conteo[color].append(fit)

    return {color: sum(valores) for color, valores in conteo.items()}

# -------------------------------------------------------------------------


def main():

    codigo_secreto = generar_codigo()
    print(f"\nCódigo secreto: {codigo_secreto}\n")

    # 3. Create initial population
    poblacion = crear_poblacion()

    # -------------------- LISTAS PARA MATPLOTLIB --------------------

    lista_intentos = []
    lista_pistas = []
    generaciones = []
    fitness_colores = {
        "rojo": [],
        "verde": [],
        "azul": [],
        "amarillo": [],
        "blanco": [],
        "negro": []
    }

    # -----------------------------------------------------------------

    generacion = 1
    while generacion <= MAX_GENERACION:
        

        #4. Measure fitness of individuals
        mejor_individuo = None
        mejor_fitness = -1
        negros = 0
        blancos = 0

        for individuo in poblacion:
            fit, n, b = calcular_fitness(individuo, codigo_secreto)
            if fit > mejor_fitness:
                mejor_individuo = individuo
                mejor_fitness = fit
                negros = n
                blancos = b

        #Mostrar intento en consola
        visual = "●" * negros + "○" * blancos
        print("Intento", generacion, ":", mejor_individuo, visual)


        # -------------------- GUARDAR DATOS PARA MATPLOTLIB --------------------

        lista_intentos.append(mejor_individuo)
        lista_pistas.append((negros, blancos))
        generaciones.append(generacion)

        #Matplotlib grafica fitness
        fitness_gen = fitness_por_color(poblacion, codigo_secreto)
        for color in fitness_colores:
            fitness_colores[color].append(fitness_gen[color])

        # ------------------------------------------------------------------------


        # Comprobar si adivino el código
        if mejor_individuo == codigo_secreto:
            print("\n¡La máquina adivinó el código en la generación", generacion, "!\n")
            break
        
        #5. Select parents
        padres = seleccionar_padres(poblacion, codigo_secreto)

        #6–7. Reproduce offspring & populate next generation
        poblacion = crear_nueva_generacion(padres) 

        generacion += 1


    # -------------------- LLAMADAS A MATPLOTLIB AL FINAL --------------------

    graficar_tablero(lista_intentos, lista_pistas, codigo_secreto)
    graficar_barras_fitness_por_generacion_y_color(generaciones, fitness_colores)
    
    # ------------------------------------------------------------------------


if __name__ == "__main__":
    main()