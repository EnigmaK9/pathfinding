import pygame
import sys

# parametros de la ventana
ANCHO = 400
ALTO = 400
tamaño_celda = 25


def dibujar_mapa_a_star(matriz):
    
    # Configuramos las dimensiones de la ventana y su título
    ventana = pygame.display.set_mode((ANCHO, ALTO))

    pygame.display.set_caption("Camino encontrado en el mapa")

    # Crear la ventana
    ventana = pygame.display.set_mode((500, 500))

    # Cargar las imagenes
    imagen_obstaculo = pygame.image.load("obstaculo.png")
    imagen_agente = pygame.image.load("agente.png")
    imagen_agente2 = pygame.image.load("agente2.png")
    imagen_meta = pygame.image.load("meta.png")
    imagen_camino = pygame.image.load("camino.png")
    imagen_camino2 = pygame.image.load("camino2.png")
    imagen_piso = pygame.image.load("piso.png")

    dibujo = {
        1: imagen_obstaculo,
        2: imagen_agente,
        3: imagen_agente2,
        5: imagen_meta,
        'x': imagen_camino,
        'y': imagen_camino2,
        0: imagen_piso
    }


    # Dibuja cada celda de matriz_caminos en su posición correspondiente
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            x = j * 25
            y = i * 25
            ventana.blit(dibujo[valor], (x, y))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()