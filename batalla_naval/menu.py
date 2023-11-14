import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos algunas constantes
ANCHO = 640
ALTO = 480

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Creamos la pantalla
ancho_pantalla = 1280
altura_pantalla = 720
pantalla = pygame.display.set_mode((ancho_pantalla, altura_pantalla), pygame.FULLSCREEN)
pygame.display.set_caption("Batalla naval")

# Cargar la imagen de fondo
background_image = pygame.image.load("batalha-naval.jpg").convert()
background_image = pygame.transform.scale(background_image, (ancho_pantalla, altura_pantalla))

# Definimos algunas constantes para el menú
MENU_FONDO = (0, 0, 255)
MENU_FONDO_SELECCIONADO = (255, 255, 255)
MENU_FONDO_NO_SELECCIONADO = (0, 0, 0)
MENU_COLOR_TEXTO = (255, 255, 255)
MENU_COLOR_TEXTO_SELECCIONADO = (0, 0, 0)
MENU_COLOR_TEXTO_NO_SELECCIONADO = (255, 255, 255)

MENU_OPCIONES = ["Comenzar juego", "Acerca de", "Salir"]
MENU_SELECCION = 0

def dibujar_menu():
    pantalla.blit(background_image, (0, 0))
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
        pantalla.blit(opcion_fondo, (x - 100, y - 20))
        opcion_texto = pygame.font.SysFont(None, 32).render(opcion, True, color_texto)
        pantalla.blit(opcion_texto, (x - opcion_texto.get_width() // 2, y - opcion_texto.get_height() // 2))
    pygame.display.flip()

def manejar_teclado(evento):
    global MENU_SELECCION
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_UP:
            MENU_SELECCION = (MENU_SELECCION - 1) % len(MENU_OPCIONES)
        elif evento.key == pygame.K_DOWN:
            MENU_SELECCION = (MENU_SELECCION + 1) % len(MENU_OPCIONES)
        elif evento.key == pygame.K_RETURN:
            if MENU_SELECCION == 0:
                comenzar_juego()
            elif MENU_SELECCION == 1:
                acerca_de()
            elif MENU_SELECCION == 2:
                salir()
        elif evento.key == pygame.K_ESCAPE:  # Agregamos esta parte para la tecla Escape
            salir()

def manejar_mouse(evento):
    global MENU_SELECCION
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # 1 significa clic izquierdo
        x, y = evento.pos
        for i, opcion in enumerate(MENU_OPCIONES):
            x_opcion = ANCHO // 2
            y_opcion = ALTO // 2 + i * 50
            ancho_opcion = 200
            alto_opcion = 40
            if x_opcion - ancho_opcion // 2 < x < x_opcion + ancho_opcion // 2 and \
               y_opcion - alto_opcion // 2 < y < y_opcion + alto_opcion // 2:
                MENU_SELECCION = i
                if MENU_SELECCION == 0:
                    comenzar_juego()
                elif MENU_SELECCION == 1:
                    acerca_de()
                elif MENU_SELECCION == 2:
                    salir()

def comenzar_juego():
    pass

def acerca_de():
    pass

def salir():
    pygame.quit()
    sys.exit()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        manejar_teclado(evento)
        manejar_mouse(evento)
    dibujar_menu()

