import os
import pygame
import sys

# Establecer el directorio de trabajo actual al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Reproducción de Sonido")

# Inicializar el módulo de sonido
pygame.mixer.init()

# Cargar el sonido que quieres reproducir
sound = pygame.mixer.Sound("disparo.mp3")

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Reproducir el sonido al hacer clic
            sound.play()

    # Actualizar la pantalla
    pygame.display.flip()
