import matplotlib.pyplot as plt
import matplotlib.patches as patches

MAPA_COLORES = {
    "rojo": "#c0392b",
    "verde": "#27ae60",
    "azul": "#2980b9",
    "amarillo": "#f1c40f",
    "blanco": "#ecf0f1",
    "negro": "#2c3e50"
}

COLOR_MADERA = "#b86b1f"
COLOR_AGUJERO = "#c0b5ac"
COLOR_PISTA_FONDO = "#8e6e53"


def graficar_tablero(intentos, pistas, codigo_secreto):
    total_filas = 14
    columnas = len(codigo_secreto)

    fig, ax = plt.subplots(figsize=(6, 11))
    fig.patch.set_facecolor("black")

    # Fondo tablero
    tablero = patches.FancyBboxPatch(
        (0, 0), 7, total_filas + 3,
        boxstyle="round,pad=0.3,rounding_size=0.6",
        facecolor=COLOR_MADERA,
        edgecolor="none"
    )
    ax.add_patch(tablero)

    # Posiciones base
    x_numero = 0.6
    x_pistas = 1.4
    x_fichas = 3.0

    # ================================
    # DIBUJAR FILAS (ARRIBA → ABAJO)
    # ================================
    for fila in range(total_filas):
        y = total_filas - fila + 1

        # Número de intento
        ax.text(
            x_numero, y,
            f"{fila + 1}",
            ha="center",
            va="center",
            fontsize=9,
            color="white",
            weight="bold"
        )

        # Agujeros fichas
        for col in range(columnas):
            agujero = plt.Circle(
                (x_fichas + col * 0.8, y),
                0.28,
                color=COLOR_AGUJERO,
                ec="black",
                lw=1
            )
            ax.add_patch(agujero)

        # Agujeros pistas
        for i in range(4):
            px = x_pistas + (i % 2) * 0.35
            py = y + (0.18 if i < 2 else -0.18)
            pista = plt.Circle(
                (px, py),
                0.1,
                color=COLOR_PISTA_FONDO,
                ec="black",
                lw=0.8
            )
            ax.add_patch(pista)

        # Intentos reales (de arriba hacia abajo)
        if fila < len(intentos):
            intento = intentos[fila]
            negros, blancos = pistas[fila]

            # Fichas
            for col, color in enumerate(intento):
                ficha = plt.Circle(
                    (x_fichas + col * 0.8, y),
                    0.28,
                    color=MAPA_COLORES[color],
                    ec="black",
                    lw=1.2
                )
                ax.add_patch(ficha)

            # Pistas negras/blancas
            k = 0
            for _ in range(negros):
                px = x_pistas + (k % 2) * 0.35
                py = y + (0.18 if k < 2 else -0.18)
                pista = plt.Circle((px, py), 0.1, color="black")
                ax.add_patch(pista)
                k += 1

            for _ in range(blancos):
                px = x_pistas + (k % 2) * 0.35
                py = y + (0.18 if k < 2 else -0.18)
                pista = plt.Circle((px, py), 0.1, color="white", ec="black")
                ax.add_patch(pista)
                k += 1

    # ================================
    # CÓDIGO SECRETO (ABAJO)
    # ================================
    y_secreto = 1

    for col, color in enumerate(codigo_secreto):
        ficha = plt.Circle(
            (x_fichas + col * 0.8, y_secreto),
            0.3,
            color=MAPA_COLORES[color],
            ec="gold",
            lw=2
        )
        ax.add_patch(ficha)

    ax.text(
        x_fichas - 1.1,
        y_secreto,
        "Código secreto",
        ha="right",
        va="center",
        fontsize=10,
        color="white",
        weight="bold"
    )


    # ================================
    # AJUSTES FINALES
    # ================================
    ax.set_xlim(0, 7)
    ax.set_ylim(0, total_filas + 3)
    ax.axis("off")

    plt.title("Mastermind", color="white", fontsize=14, pad=10)
    plt.show()

# ================================
# EVOLUCIÓN DEL FITNESS
# ================================
def graficar_fitness_por_color(generaciones, fitness_colores):
    """
    Muestra la evolución del fitness medio por color a lo largo
    de las generaciones del algoritmo genético
    """

    import matplotlib.pyplot as plt

    colores_plot = {
        "rojo": "#c0392b",
        "verde": "#27ae60",
        "azul": "#2980b9",
        "amarillo": "#f1c40f",
        "blanco": "#7f8c8d",
        "negro": "#2c3e50"
    }

    plt.figure(figsize=(10, 6))
    plt.gca().set_facecolor("#f4f4f4")

    for color, valores in fitness_colores.items():
        plt.plot(
            generaciones,
            valores,
            marker="o",
            linewidth=2,
            label=color.capitalize(),
            color=colores_plot[color]
        )

    plt.title("Evolución del Fitness Medio por Color", fontsize=14)
    plt.xlabel("Generación")
    plt.ylabel("Fitness medio de la población")
    plt.xticks(generaciones)
    plt.grid(True, alpha=0.3)
    plt.legend(title="Colores")
    plt.tight_layout()
    plt.show()