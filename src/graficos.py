import matplotlib.pyplot as plt

# Este módulo grafica la evolución del algoritmo genético para Mastermind.

def graficar_evolucion(generaciones, fitness, negros, blancos):
    """
    Genera una gráfica de la evolución del algoritmo genético.

    Parámetros:
    - generaciones: lista de números de generación
    - fitness: lista de fitness del mejor individuo por generación
    - negros: lista de pistas negras por generación
    - blancos: lista de pistas blancas por generación
    """

    fig, ax1 = plt.subplots()

    # Gráfica de fitness
    ax1.plot(generaciones, fitness, marker='o')
    ax1.set_xlabel("Generación")
    ax1.set_ylabel("Fitness (mejor individuo)")

    # Segundo eje para negros y blancos
    ax2 = ax1.twinx()
    ax2.plot(generaciones, negros, linestyle='--', marker='s')
    ax2.plot(generaciones, blancos, linestyle=':', marker='^')
    ax2.set_ylabel("Pistas (negras / blancas)")

    plt.title("Evolución del Algoritmo Genético en Mastermind")
    plt.grid(True)
    plt.show()

# ------------------------------------------------------------
#  NUEVA FUNCIÓN: Graficar TABLERO estilo Mastermind
# ------------------------------------------------------------

import matplotlib.patches as patches
import math

def graficar_tablero(intentos, pistas, codigo_secreto=None):
    """
    Dibuja un tablero estilo Mastermind con matplotlib.

    Parámetros:
    - intentos: lista de listas, cada intento es una combinación (por ejemplo ['R','G','B','Y'])
    - pistas: lista de listas con símbolos o valores de pistas (ej: [(2,1), (1,2)] )
    - codigo_secreto: lista opcional para mostrar al resolver
    """

    filas = len(intentos)
    cols = len(intentos[0]) if intentos else 4

    fig, ax = plt.subplots(figsize=(6, filas * 0.7))
    ax.set_xlim(0, cols + 3)
    ax.set_ylim(0, filas + 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Mapeo simple de colores
    mapa_colores = {
        'R': 'red',
        'G': 'green',
        'B': 'blue',
        'Y': 'yellow',
        'O': 'orange',
        'P': 'purple'
    }

    # Dibujar cada fila de intento
    for i, intento in enumerate(intentos):
        y = filas - i

        # Círculos de intento
        for j, ficha in enumerate(intento):
            color = mapa_colores.get(ficha, 'gray')
            circ = patches.Circle((j + 1, y), 0.3, facecolor=color, edgecolor='black')
            ax.add_patch(circ)

        # Pistas (negras y blancas)
        negros, blancos = pistas[i]
        x_pista = cols + 1

        # Negros → círculo negro
        for n in range(negros):
            circ = patches.Circle((x_pista, y + 0.2 * (n - 1)), 0.15, facecolor='black', edgecolor='black')
            ax.add_patch(circ)

        # Blancos → círculo blanco
        for b in range(blancos):
            circ = patches.Circle((x_pista + 0.5, y + 0.2 * (b - 1)), 0.15, facecolor='white', edgecolor='black')
            ax.add_patch(circ)

    # Mostrar código secreto si se da
    if codigo_secreto:
        ax.text(0.5, 0.3, f"Código secreto: {codigo_secreto}", fontsize=12)

    plt.title("Tablero Mastermind")
    plt.show()



# ------------------------------------------------------------
#  NUEVA FUNCIÓN: Graficar evolución del fitness
# ------------------------------------------------------------

def graficar_evolucion(generaciones, fitness, negros, blancos):
    """
    Grafica la evolución del fitness y de las pistas negras/blancas
    por generación.

    generaciones: lista de números de generación
    fitness: lista del mejor fitness por generación
    negros: lista de negros por generación
    blancos: lista de blancos por generación
    """

    plt.figure(figsize=(8, 5))
    plt.plot(generaciones, fitness, marker='o')
    plt.title("Evolución del Fitness del Algoritmo Genético")
    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.show()

    # Gráfica de pistas
    plt.figure(figsize=(8, 5))
    plt.plot(generaciones, negros, marker='s')
    plt.plot(generaciones, blancos, marker='^')
    plt.title("Evolución de Pistas: Negros y Blancos")
    plt.xlabel("Generación")
    plt.ylabel("Cantidad de pistas")
    plt.grid(True)
    plt.show()

