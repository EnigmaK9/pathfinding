import random


def crear_obstaculos_aleatorios(matriz):
    # ingrese el numero de obstaculos deseados
    numero_obstaculos = int(input("Ingrese el número de obstáculos deseados:"))
        # Generamos obstáculos
    for i in range(numero_obstaculos):
            fila = random.randint(0, 19)
            columna = random.randint(0, 19)
            matriz[fila][columna] = 1

def crear_obstaculos_fijos(matriz):
    matriz[4][2] = 1
    matriz[4][3] = 1
    matriz[3][4] = 1
    matriz[4][6] = 1
    matriz[5][7] = 1
    matriz[6][7] = 1
    matriz[7][7] = 1
    matriz[5][8] = 1
    matriz[6][8] = 1
    matriz[7][8] = 1
    matriz[8][8] = 1
    matriz[9][8] = 1
    matriz[10][8] = 1
    matriz[5][9] = 1
    matriz[9][9] = 1
    matriz[10][9] = 1
    matriz[11][9] = 1
    matriz[12][9] = 1
    matriz[13][9] = 1
    matriz[4][10] = 1
    matriz[1][11] = 1
    matriz[2][11] = 1
    matriz[3][11] = 1
    matriz[4][11] = 1
    matriz[5][11] = 1
    matriz[0][11] = 1
    matriz[7][12] = 1
    matriz[8][12] = 1
    matriz[7][13] = 1
    matriz[8][13] = 1