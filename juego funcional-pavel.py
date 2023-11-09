import pygame
import sys
import random

# Definir colores
ANCHO, ALTO = 600, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
DISPARO_FALLADO = 'O'
DISPARO_ACERTADO = 'X'

# Inicialización de Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Batalla Naval")

# Tamaño del tablero
FILAS, COLUMNAS = 10, 10
TAMANO_CELDA = 60

# Crear tablero
tablero_jugador = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]
tablero_maquina = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]
# tablero_maquina = [[0]*10 for _ in range(10)]
# tablero_jugador1 = [[0]*5 for _ in range(10)]
# tablero_jugador2 = [[0]*5 for _ in range(10)]

# Colocar barcos al azar
def colocar_barcos(tablero):
    for _ in range(6):
        fila, columna = random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)
        tablero[fila][columna] = "B"

# Función para dibujar el tablero de la máquina (sin mostrar barcos)
def dibujar_tablero_maquina(tablero):
    # fondo = pygame.image.load("Mar-3161677646/fondo.png")
    # ventana.blit(fondo, (0, 0))
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(ventana, ROJO, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)
            if tablero[fila][columna] == DISPARO_FALLADO:
                pygame.draw.circle(ventana, AMARILLO, (columna * TAMANO_CELDA + TAMANO_CELDA // 2, fila * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 6)
            elif tablero[fila][columna] == DISPARO_ACERTADO:
                pygame.draw.line(ventana, NEGRO, (columna * TAMANO_CELDA, fila * TAMANO_CELDA), (columna * TAMANO_CELDA + TAMANO_CELDA, fila * TAMANO_CELDA + TAMANO_CELDA), 2)
                pygame.draw.line(ventana, NEGRO, (columna * TAMANO_CELDA, fila * TAMANO_CELDA + TAMANO_CELDA), (columna * TAMANO_CELDA + TAMANO_CELDA, fila * TAMANO_CELDA), 2)


# Función para dibujar el tablero del jugador
def dibujar_tablero_jugador(tablero):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            pygame.draw.rect(ventana, NEGRO, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)
            if tablero[fila][columna] == 'B':
                pygame.draw.circle(ventana, NEGRO, (columna * TAMANO_CELDA + TAMANO_CELDA // 2, fila * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 3)
    
# Obtener coordenadas de celda a partir de clic del mouse
def obtener_celda_clic(posicion_mouse):
    x, y = posicion_mouse
    fila = y // TAMANO_CELDA
    columna = x // TAMANO_CELDA
    return fila, columna

# Disparo del jugador
def Disparo_jugador(fila, columna):
    if tablero_maquina[fila][columna] == 'B':
        print("¡Barco enemigo hundido!")
        tablero_maquina[fila][columna] = DISPARO_ACERTADO
    else:
        print("Agua...")
        tablero_maquina[fila][columna] = DISPARO_FALLADO

# Procesar disparo de la máquina (IA simple)
def Disparo_maquina():
    while True:
        fila, columna = random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)
        # pygame.time.delay(2000)
        if tablero_jugador[fila][columna] == 'B':
            print("¡Tu barco ha sido alcanzado!")
            tablero_jugador[fila][columna] = DISPARO_ACERTADO
            break
        elif tablero_jugador[fila][columna] == ' ':
            print("La máquina dispara al agua...")
            tablero_jugador[fila][columna] = DISPARO_FALLADO
            break

# Función para verificar si todos los barcos han sido hundidos
def todos_los_barcos_hundidos(tablero):
    for fila in tablero:
        if 'B' in fila:
            return False
    return True

# Bucle principal del juego
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
turno_jugador = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and turno_jugador:
            if evento.button == 1:  # Clic izquierdo
                fila, columna = obtener_celda_clic(evento.pos)
                Disparo_jugador(fila, columna)
                turno_jugador = False

    if not turno_jugador:
        Disparo_maquina()
        turno_jugador = True

    ventana.fill(BLANCO)
    dibujar_tablero_jugador(tablero_jugador)
    dibujar_tablero_maquina(tablero_maquina)
    pygame.display.flip()

    if todos_los_barcos_hundidos(tablero_jugador):
        print("¡Perdiste! Todos tus barcos han sido hundidos.")
        break
    elif todos_los_barcos_hundidos(tablero_maquina):
        print("¡Ganaste! Todos los barcos enemigos han sido hundidos.")
        break