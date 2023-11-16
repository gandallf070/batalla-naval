# import pygame
# import sys

# # Inicializa Pygame
# pygame.init()

# # Definir colores
# NEGRO = (0, 0, 0)
# BLANCO = (255, 255, 255)

# # Configuración de la pantalla
# ancho_pantalla = 800
# alto_pantalla = 600
# pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
# pygame.display.set_caption("Menú de Juego")

# # Función para mostrar texto en la pantalla
# def mostrar_texto(texto, x, y, tamano, color):
#     fuente = pygame.font.Font(None, tamano)
#     texto_renderizado = fuente.render(texto, True, color)
#     pantalla.blit(texto_renderizado, (x, y))

# # Función del menú
# def menu():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     return  # Sale del bucle del menú al presionar espacio

#         # Limpia la pantalla
#         pantalla.fill(NEGRO)

#         # Muestra el título del menú
#         mostrar_texto("¡Bienvenido al Juego!", 250, 150, 40, BLANCO)

#         # Muestra las opciones del menú
#         mostrar_texto("Presiona ESPACIO para jugar", 250, 300, 30, BLANCO)
#         mostrar_texto("Presiona ESC para salir", 250, 350, 30, BLANCO)

#         # Actualiza la pantalla
#         pygame.display.flip()

# # Bucle principal del juego
# def bucle_principal():
#     # Coloca tu código de juego aquí
#     print("copie el juego aquí")
#     # ...

# # Llama al menú
# menu()

# # Después de salir del menú (presionar espacio), inicia el bucle principal del juego
# bucle_principal()
import pygame
import sys
import os

# Inicializa Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Imprime el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())

# Configuración de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Menú de Juego")

# Cargar video
video_path = "video.mp4"
if os.path.exists(video_path):
    pygame.mixer.quit()  # Detener la música para reproducir el video
    pygame.display.quit()  # Cerrar la ventana actual antes de reproducir el video
    os.system(f"start vlc {video_path}")  # Utiliza VLC u otro reproductor para el video
    sys.exit()
else:
    print(f"No se pudo encontrar el archivo de video: {video_path}")

# Cargar música
pygame.mixer.init()
pygame.mixer.music.load("sonido.mp3")
pygame.mixer.music.play(-1)  # -1 indica reproducción en bucle

# Función para mostrar texto en la pantalla
def mostrar_texto(texto, x, y, tamano, color):
    fuente = pygame.font.Font(None, tamano)
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

# Función del menú
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Sale del bucle del menú al presionar espacio

        # Limpia la pantalla
        pantalla.fill(NEGRO)

        # Muestra el título del menú
        mostrar_texto("¡Bienvenido al Juego!", 250, 150, 40, BLANCO)

        # Muestra las opciones del menú
        mostrar_texto("Presiona ESPACIO para jugar", 250, 300, 30, BLANCO)
        mostrar_texto("Presiona ESC para salir", 250, 350, 30, BLANCO)

        # Actualiza la pantalla
        pygame.display.flip()

# Bucle principal del juego
def bucle_principal():
    # Coloca tu código de juego aquí
    print("copie el juego aquí")
    # ...

# Llama al menú
menu()

# Después de salir del menú (presionar espacio), inicia el bucle principal del juego
bucle_principal()
