# Historias de Usuario – Mastermind con Algoritmo Genético

## Historia de Usuario 1 – Generación del código secreto
**Como** jugador,  
**quiero** que el sistema genere un código secreto de 4 colores al inicio de la partida,  
**para** que la máquina tenga un objetivo a adivinar.  

**Criterios de aceptación:**  
- El código secreto se genera aleatoriamente de entre los colores disponibles.  
- La longitud del código es configurable (por defecto, 4).  
- El código se mantiene oculto hasta que la máquina adivine o termine la partida.  

---

## Historia de Usuario 2 – Visualizar combinaciones de la máquina
**Como** usuario,  
**quiero** ver las combinaciones que propone la máquina en cada generación,  
**para** seguir el progreso del algoritmo genético y entender cómo se acerca al código secreto.  

**Criterios de aceptación:**  
- Cada generación muestra en consola la mejor combinación propuesta y su valor de fitness.  
- Se indica el número de generación correspondiente.  

---

## Historia de Usuario 3 – Evaluación de fitness
**Como** desarrollador,  
**quiero** una función de fitness que compare cada individuo con el código secreto,  
**para** que el algoritmo genético pueda seleccionar las mejores combinaciones.  

**Criterios de aceptación:**  
- La función debe contar aciertos exactos (color y posición).  
- Debe contar aciertos de color en posición incorrecta.  
- No debe modificar los individuos ni el código original durante la evaluación.  

---

## Historia de Usuario 4 – Selección de padres
**Como** desarrollador,  
**quiero** un mecanismo de selección (torneo) para elegir los mejores individuos,  
**para** que la reproducción del algoritmo genético favorezca combinaciones más cercanas al código secreto.  

**Criterios de aceptación:**  
- La mitad de la población es seleccionada en cada generación.  
- La selección se basa en el valor de fitness de los individuos.  

---

## Historia de Usuario 5 – Cruce de individuos
**Como** desarrollador,  
**quiero** una función de cruce (un punto) para generar hijos a partir de dos padres,  
**para** combinar características de individuos con buen fitness y mejorar la población.  

**Criterios de aceptación:**  
- El cruce debe devolver dos hijos.  
- Cada hijo conserva parte de cada padre según el punto de cruce.  

---

## Historia de Usuario 6 – Mutación
**Como** desarrollador,  
**quiero** una función de mutación que altere aleatoriamente un color en un individuo según una probabilidad,  
**para** mantener diversidad genética y evitar estancamiento del algoritmo.  

**Criterios de aceptación:**  
- La mutación no debe modificar la lista original del individuo.  
- El color resultante debe ser válido.  
- Todas las posiciones del individuo pueden ser mutadas eventualmente.  

---

## Historia de Usuario 7 – Ejecución del algoritmo genético
**Como** usuario,  
**quiero** que la máquina ejecute el algoritmo genético hasta adivinar el código o alcanzar el límite de generaciones,  
**para** ver el proceso completo de resolución del Mastermind.  

**Criterios de aceptación:**  
- El algoritmo se detiene si la máquina adivina el código.  
- Se muestra en consola la evolución de la población generación a generación.  
- Se informa si no se adivinó el código al alcanzar el límite de generaciones.  