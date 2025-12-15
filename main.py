from src.constantes import max_generaciones
from src.generar_codigo_secreto import generar_codigo
from src.crear_poblacion import crear_poblacion
from src.fitness import calcular_fitness
from src.seleccion_padres import seleccionar_padres
from src.nueva_generacion import crear_nueva_generacion

# -------------------- IMPORTAR FUNCIONES DE MATPLOTLIB --------------------
from src.graficos import graficar_tablero, graficar_barras_fitness_por_generacion_y_color
import matplotlib
matplotlib.use("TkAgg")  # Forzar backend que abre ventana de gráficos
# -------------------------------------------------------------------------

def fitness_por_color(poblacion, codigo_secreto):
    colores = ["rojo", "verde", "azul", "amarillo", "blanco", "negro"]
    conteo = {color: [] for color in colores}

    for individuo in poblacion:
        fit, _, _ = calcular_fitness(individuo, codigo_secreto)
        for color in set(individuo):
            conteo[color].append(fit)

    return {
        color: sum(valores)
        for color, valores in conteo.items()
    }


def main():

    codigo_secreto = generar_codigo()
    print(f"Código secreto: {codigo_secreto}\n")

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
    while generacion <= max_generaciones:

        mejor = poblacion[0]
        mejor_fitness, negros, blancos = calcular_fitness(mejor, codigo_secreto)

        for individuo in poblacion:
            fit, n, b = calcular_fitness(individuo, codigo_secreto)
            if fit > mejor_fitness:
                mejor = individuo
                mejor_fitness = fit
                negros = n
                blancos = b

        # Mostrar intento en consola
        visual = "●" * negros + "○" * blancos + " " * (len(codigo_secreto) - negros - blancos)
        print("Intento", generacion, ":", mejor, visual)

        # -------------------- GUARDAR DATOS PARA MATPLOTLIB --------------------
        lista_intentos.append(mejor)
        lista_pistas.append((negros, blancos))
        generaciones.append(generacion)

        # Matplotlib grafica fitness
        fitness_gen = fitness_por_color(poblacion, codigo_secreto)
        for color in fitness_colores:
            fitness_colores[color].append(fitness_gen[color])
        # ------------------------------------------------------------------------

        if mejor == codigo_secreto:
            print("\n¡La máquina adivinó el código en la generación", generacion, "!")
            # No retornamos aquí; dejamos que los gráficos se muestren
            break

        padres = seleccionar_padres(poblacion, codigo_secreto)
        poblacion = crear_nueva_generacion(padres)
        generacion += 1

    print("\nFin del juego.")

    # -------------------- LLAMADAS A MATPLOTLIB AL FINAL --------------------
    graficar_tablero(lista_intentos, lista_pistas, codigo_secreto)
    graficar_barras_fitness_por_generacion_y_color(generaciones, fitness_colores)
    # ------------------------------------------------------------------------

if __name__ == "__main__":
    main()
