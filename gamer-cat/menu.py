import pygame
import sys

# Inicializa Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla),pygame.RESIZABLE)
pygame.display.set_caption("Menú de Juego")

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
#                 if event.key == pygame.K_RETURN:
#                     # Iniciar juego (código del juego)
#                     print("Pegue aquí su código para iniciar el juego")
#                 elif event.key == pygame.K_SPACE:
#                     # Mostrar créditos de los desarrolladores (código de créditos)
#                     print("Pegue aquí su código para mostrar créditos de los desarrolladores")
#                 elif event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()

#         # Limpia la pantalla
#         pantalla.fill(NEGRO)

#         # Muestra el título del menú
#         mostrar_texto("¡Bienvenido al Juego!", 250, 150, 40, BLANCO)

#         # Muestra las opciones del menú
#         mostrar_texto("Presiona ENTER para iniciar el juego", 250, 300, 30, BLANCO)
#         mostrar_texto("Presiona ESPACIO para créditos de los desarrolladores", 250, 350, 30, BLANCO)
#         mostrar_texto("Presiona ESCAPE para salir", 250, 400, 30, BLANCO)

#         # Actualiza la pantalla
#         pygame.display.flip()

# # Llama al menú
# menu()
# import pygame
# import sys
# import cv2

# # Inicializa Pygame
# pygame.init()
# surface = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Menú de Juego")

# # Cargar recursos multimedia
# fondo = pygame.image.load("imagen.jpeg")
# sonido_menu = pygame.mixer.Sound("sonido.mp3")
# video_intro = "video.mp4"
# video_acercade = "video3.mp4"
# video_fin_juego = "video2.mp4"

# # Definir la función para mostrar texto en la pantalla
# def mostrar_texto(texto, x, y, tamano, color):
#     fuente = pygame.font.Font(None, tamano)
#     texto_renderizado = fuente.render(texto, True, color)
#     surface.blit(texto_renderizado, (x, y))

# # Función para reproducir video de manera síncrona
# def reproducir_video(video_path, next_function):
#     pygame.mixer.stop()
#     pygame.time.delay(1000)  # Espera 1 segundo para asegurar que el sonido del menú esté desactivado
#     pygame.display.set_caption("Reproduciendo Video")

#     cap = cv2.VideoCapture(video_path)

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame = pygame.surfarray.make_surface(frame)
#         surface.blit(frame, (0, 0))
#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#     cap.release()
#     pygame.display.set_caption("Menú de Juego")

#     # Lógica para volver al menú después del video
#     next_function()

# # Funciones de eventos al presionar las opciones del menú
# def iniciar_juego():
#     reproducir_video(video_intro, jugar)

# def acerca_de():
#     reproducir_video(video_acercade, mostrar_menu)

# def salir():
#     pygame.quit()
#     sys.exit()

# # Funciones para volver al menú después de los videos
# def mostrar_menu():
#     pygame.mixer.Sound.play(sonido_menu)
#     surface.blit(fondo, (0, 0))
#     mostrar_texto("Presiona Enter para Iniciar Juego", 200, 200, 30, (255, 255, 255))
#     mostrar_texto("Presiona Espacio para Acerca de", 200, 250, 30, (255, 255, 255))
#     mostrar_texto("Presiona Escape para Salir", 200, 300, 30, (255, 255, 255))
#     pygame.display.flip()

# def jugar():
#     print("Inicia el juego aquí")  # Coloca tu código del juego aquí
#     reproducir_video(video_fin_juego, mostrar_menu)

# # Mostrar opciones de menú al inicio
# mostrar_menu()

# # Bucle principal del menú
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 iniciar_juego()
#             elif event.key == pygame.K_SPACE:
#                 acerca_de()
#             elif event.key == pygame.K_ESCAPE:
#                 salir()
# import pygame
# import sys
# import cv2

# # Inicializa Pygame
# pygame.init()

# # Obtener la resolución del monitor principal
# screen_info = pygame.display.Info()
# ancho_pantalla = screen_info.current_w
# alto_pantalla = screen_info.current_h

# # Inicializa la pantalla en modo ventana
# surface = pygame.display.set_mode((ancho_pantalla, alto_pantalla), pygame.RESIZABLE)
# pygame.display.set_caption("Menú de Juego")

# # Cargar recursos multimedia
# fondo = pygame.image.load("imagen.jpeg")
# sonido_menu = pygame.mixer.Sound("sonido.mp3")
# video_intro = "video.mp4"
# video_acercade = "video3.mp4"
# video_fin_juego = "video2.mp4"

# # Definir la función para mostrar texto en la pantalla
# def mostrar_texto(texto, x, y, tamano, color):
#     fuente = pygame.font.Font(None, tamano)
#     texto_renderizado = fuente.render(texto, True, color)
#     surface.blit(texto_renderizado, (x, y))

# # Función para reproducir video de manera síncrona
# def reproducir_video(video_path, next_function):
#     pygame.mixer.stop()
#     pygame.time.delay(1000)  # Espera 1 segundo para asegurar que el sonido del menú esté desactivado
#     pygame.display.set_caption("Reproduciendo Video")

#     cap = cv2.VideoCapture(video_path)

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = cv2.flip(frame, 1)  # Voltear horizontalmente (modo espejo)
#         frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotar 90 grados a la izquierda
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame = pygame.surfarray.make_surface(frame)
#         surface.blit(frame, (0, 0))
#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#     cap.release()
#     pygame.display.set_caption("Menú de Juego")

#     # Lógica para volver al menú después del video
#     next_function()

# # Funciones de eventos al presionar las opciones del menú
# def iniciar_juego():
#     reproducir_video(video_intro, jugar)

# def acerca_de():
#     reproducir_video(video_acercade, mostrar_menu)

# def salir():
#     pygame.quit()
#     sys.exit()

# # Funciones para volver al menú después de los videos
# def mostrar_menu():
#     pygame.mixer.Sound.play(sonido_menu)
#     surface.blit(fondo, (0, 0))
#     mostrar_texto("Presiona Enter para Iniciar Juego", 200, 200, 30, (255, 255, 255))
#     mostrar_texto("Presiona Espacio para Acerca de", 200, 250, 30, (255, 255, 255))
#     mostrar_texto("Presiona Escape para Salir", 200, 300, 30, (255, 255, 255))
#     pygame.display.flip()

# def jugar():
#     print("Inicia el juego aquí")  # Coloca tu código del juego aquí
#     reproducir_video(video_fin_juego, mostrar_menu)

# # Mostrar opciones de menú al inicio
# mostrar_menu()

# # Bucle principal del menú
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 iniciar_juego()
#             elif event.key == pygame.K_SPACE:
#                 acerca_de()
#             elif event.key == pygame.K_ESCAPE:
#                 salir()
#             elif event.key == pygame.K_f:  # Presionar 'f' para alternar entre fullscreen y ventana
#                 pygame.display.toggle_fullscreen()
# import pygame
# import sys
# import cv2

# # Inicializa Pygame
# pygame.init()

# # Obtener la resolución del monitor principal
# screen_info = pygame.display.Info()
# ancho_pantalla = screen_info.current_w
# alto_pantalla = screen_info.current_h

# # Define la resolución de la ventana de Pygame
# ventana_ancho = 800
# ventana_alto = 600

# # Calcula la escala para ajustar el video en la ventana
# escala_x = ventana_ancho / ancho_pantalla
# escala_y = ventana_alto / alto_pantalla

# # Inicializa la pantalla en modo ventana
# surface = pygame.display.set_mode((ventana_ancho, ventana_alto), pygame.APPACTIVE)
# pygame.display.set_caption("Menú de Juego")

# # Cargar recursos multimedia
# fondo = pygame.image.load("imagen.jpg")
# #sonido_menu = pygame.mixer.Sound("sonido.mp3")
# video_intro = "video.mp4"
# video_acercade = "video3.mp4"
# video_fin_juego = "video2.mp4"

# # Definir la función para mostrar texto en la pantalla
# def mostrar_texto(texto, x, y, tamano, color):
#     fuente = pygame.font.Font(None, tamano)
#     texto_renderizado = fuente.render(texto, True, color)
#     surface.blit(texto_renderizado, (x, y))

# # Función para reproducir video de manera síncrona
# def reproducir_video(video_path, next_function):
#     #pygame.mixer.stop()
#     #pygame.time.delay(1000)  # Espera 1 segundo para asegurar que el sonido del menú esté desactivado
#     pygame.display.set_caption("Reproduciendo Video")

#     cap = cv2.VideoCapture(video_path)

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Escala el frame para que se ajuste en la ventana
#         frame = cv2.resize(frame, None, fx=escala_x, fy=escala_y)
        
#         frame = cv2.flip(frame, 1)  # Voltear horizontalmente (modo espejo)
#         frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotar 90 grados a la izquierda
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame = pygame.surfarray.make_surface(frame)
#         surface.blit(frame, (0, 0))
#         pygame.display.flip()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#     cap.release()
#     pygame.display.set_caption("Menú de Juego")

#     # Lógica para volver al menú después del video
#     next_function()

# # Funciones de eventos al presionar las opciones del menú
# def iniciar_juego():
#     reproducir_video(video_intro, jugar)
# def acerca_de():
#     reproducir_video(video_acercade, mostrar_menu)

# def salir():
#     pygame.quit()
#     sys.exit()

# # Funciones para volver al menú después de los videos
# def mostrar_menu():
#     #pygame.mixer.Sound.play(sonido_menu)
#     surface.blit(fondo, (0, 0))
#     mostrar_texto("Presiona Enter para Iniciar Juego", 200, 200, 30, (255, 255, 255))
#     mostrar_texto("Presiona Espacio para Acerca de", 200, 250, 30, (255, 255, 255))
#     mostrar_texto("Presiona Escape para Salir", 200, 300, 30, (255, 255, 255))
#     pygame.display.flip()

# def jugar():
#     #print("Inicia el juego aquí")  # Coloca tu código del juego aquí
#     #juego()
#     reproducir_video(video_fin_juego, mostrar_menu)

# # Mostrar opciones de menú al inicio
# mostrar_menu()

# # Bucle principal del menú
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 iniciar_juego()
#             elif event.key == pygame.K_SPACE:
#                 acerca_de()
#             elif event.key == pygame.K_ESCAPE:
#                 salir()
#             elif event.key == pygame.K_f:  # Presionar 'f' para alternar entre fullscreen y ventana
#                 pygame.display.toggle_fullscreen()
