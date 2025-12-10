from src.generar_codigo_secreto import generar_codigo
from src.crear_poblacion import crear_poblacion
from src.ejecutar_algoritmo_genetico import ejecutar_algoritmo_genetico

def evaluar_intento(intento, codigo_secreto):
    negros = 0
    blancos = 0

    #contar negros
    i = 0
    while i < len(intento):
        if intento[i] == codigo_secreto[i]:
            negros = negros + 1
        i = i + 1

    #preparar listas para contar blancos (sin incluir los negros)
    secreto_restante = []
    intento_restante = []
    i = 0
    while i < len(intento):
        if intento[i] != codigo_secreto[i]:
            secreto_restante.append(codigo_secreto[i])
            intento_restante.append(intento[i])
        i = i + 1

    #contar blancos
    i = 0
    while i < len(intento_restante):
        color = intento_restante[i]
        j = 0
        while j < len(secreto_restante):
            if color == secreto_restante[j]:
                blancos = blancos + 1   
                #eliminamos el color encontrado para que no se cuente otra vez
                secreto_restante.pop(j)
                break  #salimos del bucle j, pasamos al siguiente color
            else:
                j = j + 1
        i = i + 1

    return negros, blancos



def mostrar_intento(numero, intento, negros, blancos):
    colores = ""
    i = 0
    while i < len(intento):
        colores = colores + intento[i]
        if i < len(intento) - 1:
            colores = colores + " | "
        i = i + 1

    pines = ""
    i = 0
    while i < negros:
        pines = pines + "●"
        i = i + 1
    i = 0
    while i < blancos:
        pines = pines + "○"
        i = i + 1

    print("Intento " + str(numero) + ": " + colores + "   " + pines)

def main():
    codigo_secreto = generar_codigo()
    poblacion = crear_poblacion()

    print("\n--- MASTER MIND ---\n")
    print("Colores posibles:")
    i = 0
    while i < len(codigo_secreto):
        print(" - " + codigo_secreto[i])
        i = i + 1
    print("\nIniciando partida...\n")

    generacion = 1
    while generacion <= 14:
        resultado = ejecutar_algoritmo_genetico(codigo_secreto, poblacion, max_generaciones=1)
        mejor = resultado[0]

        negros, blancos = evaluar_intento(mejor, codigo_secreto)
        mostrar_intento(generacion, mejor, negros, blancos)

        if negros == len(codigo_secreto):
            print("\n¡La máquina adivinó el código en el intento " + str(generacion) + "!")
            break

        generacion = generacion + 1

    print("\nCódigo secreto era:")
    i = 0
    texto = ""
    while i < len(codigo_secreto):
        texto = texto + codigo_secreto[i]
        if i < len(codigo_secreto) - 1:
            texto = texto + " | "
        i = i + 1
    print(texto)

if __name__ == "__main__":
    main()

