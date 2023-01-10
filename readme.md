# Pathfinding
Este código crea una matriz de 20x20 y asigna valores aleatorios de 0 y 1 para generar obstáculos en la matriz. Luego, se establecen las posiciones iniciales de dos agentes A1 y A2 en la matriz con los valores 2 y 3 respectivamente. Finalmente, se implementa el algoritmo de Dijkstra en una función para calcular el camino más corto desde una posición inicial a una posición destino.
## Paso 1
En el primer paso, se crea una matriz de 20x20 y se asignan aleatoriamente 24 obstáculos con el valor 1, y se imprime la matriz.
## Paso 2
En el segundo paso, se establecen las posiciones iniciales de los agentes A1 y A2 y se marcan en la matriz con los valores 2 y 3 respectivamente.
## Paso 3
En el tercer paso, se implementa una función llamada "aplicar_dijkstra" que utiliza el algoritmo de Dijkstra para encontrar el camino más corto entre una posición inicial y una posición destino. Esto se logra a través del uso de una cola de prioridad para explorar el vecino más cercano y actualizando la distancia más corta para cada celda en la matriz.


