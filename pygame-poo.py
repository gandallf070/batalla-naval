import pygame

# Inicializa Pygame
pygame.init()

# Define el tamaño de la pantalla y la matriz
screen_width, screen_height = 800, 600
cell_size = 40
rows, cols = screen_height // cell_size, screen_width // cell_size

# Crea la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))

# Crea una matriz con las coordenadas de cada celda y su color
matrix = [[{'pos': (j*cell_size, i*cell_size), 'color': (255, 255, 255)} for j in range(cols)] for i in range(rows)]

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtiene la posición del ratón y la convierte a coordenadas de la matriz
            mouse_x, mouse_y = pygame.mouse.get_pos()
            i, j = mouse_y // cell_size, mouse_x // cell_size

            # Cambia el color de la celda y imprime su posición
            matrix[i][j]['color'] = (255, 0, 0)
            print(f'Has hecho clic en la celda ({i}, {j})')

    # Dibuja la matriz en la pantalla
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(screen, matrix[i][j]['color'], (matrix[i][j]['pos'][0], matrix[i][j]['pos'][1], cell_size, cell_size), 1)

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()
