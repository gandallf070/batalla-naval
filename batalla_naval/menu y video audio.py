import pygame
import sys
import numpy as np
import cv2

# Configuración de Pygame
pygame.init()
clock = pygame.time.Clock()

# Configuración del video de fondo
video_file = "batalla.mp4"
cap = cv2.VideoCapture(video_file)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Configuración del audio
pygame.mixer.init()
pygame.mixer.music.load("Rammstein - Du hast.mp3")
pygame.mixer.music.set_volume(0.5)

# Configuración de la pantalla de Pygame
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Video Background")

# Configuración del menú
ANCHO = 640
ALTO = 480
MENU_FONDO = (0, 0, 255)
MENU_FONDO_SELECCIONADO = (255, 255, 255)
MENU_FONDO_NO_SELECCIONADO = (0, 0, 0)
MENU_COLOR_TEXTO = (255, 255, 255)
MENU_COLOR_TEXTO_SELECCIONADO = (0, 0, 0)
MENU_COLOR_TEXTO_NO_SELECCIONADO = (255, 255, 255)

MENU_OPCIONES = ["Comenzar juego", "Acerca de", "Salir"]
MENU_SELECCION = 0

background_image = pygame.image.load("batalha-naval.jpg").convert()
background_image = pygame.transform.scale(background_image, (width, height))

juego_iniciado = False

def dibujar_menu():
    screen.blit(background_image, (0, 0))
    for i, opcion in enumerate(MENU_OPCIONES):
        x = ANCHO // 2
        y = ALTO // 2 + i * 50
        if i == MENU_SELECCION:
            color_fondo = MENU_FONDO_SELECCIONADO
            color_texto = MENU_COLOR_TEXTO_SELECCIONADO
        else:
            color_fondo = MENU_FONDO_NO_SELECCIONADO
            color_texto = MENU_COLOR_TEXTO_NO_SELECCIONADO
        opcion_fondo = pygame.Surface((200, 40))
        opcion_fondo.fill(color_fondo)
        screen.blit(opcion_fondo, (x - 100, y - 20))
        opcion_texto = pygame.font.SysFont(None, 32).render(opcion, True, color_texto)
        screen.blit(opcion_texto, (x - opcion_texto.get_width() // 2, y - opcion_texto.get_height() // 2))
    pygame.display.flip()

def manejar_teclado(evento):
    global MENU_SELECCION, juego_iniciado
    if not juego_iniciado:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                MENU_SELECCION = (MENU_SELECCION - 1) % len(MENU_OPCIONES)
            elif evento.key == pygame.K_DOWN:
                MENU_SELECCION = (MENU_SELECCION + 1) % len(MENU_OPCIONES)
            elif evento.key == pygame.K_RETURN:
                if MENU_SELECCION == 0:
                    iniciar_juego()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

def manejar_mouse(evento):
    global MENU_SELECCION, juego_iniciado
    if not juego_iniciado:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x, y = evento.pos
            for i, opcion in enumerate(MENU_OPCIONES):
                x_opcion = ANCHO // 2
                y_opcion = ALTO // 2 + i * 50
                ancho_opcion = 200
                alto_opcion = 40
                if x_opcion - ancho_opcion // 2 < x < x_opcion + ancho_opcion // 2 and \
                   y_opcion - alto_opcion // 2 < y < y_opcion + alto_opcion // 2:
                    if MENU_SELECCION == 0:
                        iniciar_juego()

def iniciar_juego():
    global juego_iniciado
    juego_iniciado = True
    pygame.mixer.music.play(-1)

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            manejar_teclado(event)
            manejar_mouse(event)

        # Visualización de fondo de video
        if juego_iniciado:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out_frame = pygame.surfarray.make_surface(np.transpose(frame_rgb, (1, 0, 2)))
            screen.blit(out_frame, (0, 0))
            pygame.display.flip()
            clock.tick(fps)

       # Visualización del menú
        if not juego_iniciado:
            dibujar_menu()

finally:
    cap.release()
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()
