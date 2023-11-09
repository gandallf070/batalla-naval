import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO, ALTO = 1100, 600
screen = pygame.display.set_mode((ANCHO, ALTO))

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)

# Definir matrices
enemigo = [[0]*10 for _ in range(10)]
jugador1 = [[0]*5 for _ in range(10)]
jugador2 = [[0]*5 for _ in range(10)]

memoria_enemigo = [[0]*10 for _ in range(10)]

memoria_jugador1 = [[0]*5 for _ in range(10)]
memoria_jugador2 = [[0]*5 for _ in range(10)]

posición_enemigo=[[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
posición_jugador1=[[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
posición_jugador2=[[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(10):
    for j in range(5):
        jugador1[i][j]=posición_jugador1[i][j]
        jugador2[i][j]=posición_jugador2[i][j]
for i in range(10):
    for j in range(10):
        enemigo[i][j]=posición_enemigo[i][j]


# Definir tamaño de las celdas
tamaño_celda = 50

# Dibujar matrices
def draw_matrix(matrix, top_left, color, border_color):
    fila, columna = len(matrix), len(matrix[0])
    for i in range(fila):
        for j in range(columna):
            if matrix[i][j] == 0:
                pygame.draw.rect(screen, color, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda), 1)
                
            else:
                pygame.draw.rect(screen, AMARILLO, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda))
    pygame.draw.rect(screen, border_color, pygame.Rect(top_left[0], top_left[1], columna*tamaño_celda, fila*tamaño_celda), 3)  

def draw_jugador(memoria, top_left, color, border_color):
    fila, columna = len(memoria), len(memoria[0])
    for i in range(fila):
        for j in range(columna):
            if memoria[i][j] == 0:
                pygame.draw.rect(screen, BLANCO, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda))
                pygame.draw.rect(screen, color, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda), 2)
            
    
    pygame.draw.rect(screen, border_color, pygame.Rect(top_left[0], top_left[1], columna*tamaño_celda, fila*tamaño_celda), 3)

# Cambiar aleatoriamente una celda de una matriz
# def random_change(matrix):
#     fila, columna = len(matrix), len(matrix[0])
#     i = random.randint(0, fila - 1)
#     j = random.randint(0, columna - 1)
#     matrix[i][j] = 1

# Bucle principal
running = True
# random_change(jugador1)
# random_change(jugador2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 50 <= x <= 50 + 10*tamaño_celda and 50 <= y <= 50 + 10*tamaño_celda:
                i = (y - 50) // tamaño_celda
                j = (x - 50) // tamaño_celda
                if enemigo[i][j] == 0:
                    enemigo[i][j] = 1
                    print(f'Has hecho clic en la celda ({i}, {j}) de la matriz "enemigo".')

    screen.fill(BLANCO)


    font = pygame.font.Font(None, 36)
    text = font.render('Enemigo', 1, (10, 10, 10))
    screen.blit(text, (50, 10))
    draw_matrix(enemigo, (50, 50), ROJO, NEGRO)
    draw_jugador( memoria_enemigo, (50, 50), ROJO, NEGRO)

    text = font.render('Jugador 1', 1, (10, 10, 10))
    screen.blit(text, (50 + 10*tamaño_celda, 10))
    draw_matrix(jugador1, (50 + 10*tamaño_celda, 50), VERDE, NEGRO)

    text = font.render('Jugador 2', 1, (10, 10, 10))
    screen.blit(text, (50 + 15*tamaño_celda, 10))
    draw_matrix(jugador2, (50 + 15*tamaño_celda, 50), AZUL, NEGRO)

    pygame.display.flip()

pygame.quit()
