import pygame
import sys
import os
import cv2
import random
# Inicializar pygame
pygame.init()

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Crear pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu de Juego")

# Cargar imágenes y sonido
background_image = pygame.image.load("imagen.jpg")

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Función para reproducir un video
def play_video(video_path):
    if not pygame.display.get_init():
        return

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        
        if pygame.display.get_init():
            screen.blit(frame, (0, 0))
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # Salir de la función si se presiona ESC

    cap.release()

# Función principal del menú
def main_menu():
    pygame.mixer.init()  # Inicializar pygame.mixer
    pygame.mixer.music.load("sonido.mp3")
    
    # Pequeña pausa antes de reproducir la música
    pygame.time.delay(100)
    
    pygame.mixer.music.play(-1)  # Reproducir sonido de fondo en bucle
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Opción 1
                    pygame.mixer.music.stop()  # Detener sonido de fondo
                    play_video("video.mp4")
                    play_game()
                    play_video("video2.mp4")
                    #pygame.mixer.music.play(-1)  # Reproducir sonido de fondo al volver al menú
                elif event.key == pygame.K_SPACE:  # Opción 2
                    pygame.mixer.music.stop()  # Detener sonido de fondo
                    play_video("video3.mp4")
                    credits()
                    pygame.mixer.music.play(-1)  # Reproducir sonido de fondo al volver al menú
                elif event.key == pygame.K_ESCAPE:  # Opción 3
                    pygame.quit()
                    sys.exit()

        if pygame.display.get_init():
            screen.blit(background_image, (0, 0))
            draw_text("1. Iniciar juego (Enter)", font, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text("2. Créditos (Espacio)", font, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("3. Salir (Escape)", font, (0, 0, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

            pygame.display.flip()
            clock.tick(30)

# Función para jugar el juego principal
def play_game():
    
    class area():
        def __init__(self,n,m,vida,posicion_fila,posicion_columna,nombre):
            self.nombre=nombre
            self.fila=n
            self.columna=m
            self.vida=vida
            self.posicion_fila=posicion_fila
            self.posicion_columna=posicion_columna

        def posicion(self):
            posicion=[self.posicion_fila,self.posicion_columna]
            return posicion

        def llenar_matriz(self):
            matriz=[0]*self.fila
            for i in range(self.fila):
                lista=[0]*self.columna
                for j in range(self.columna):
                    lista[j]=0
                matriz[i]=lista
            return matriz

        def cargar_jugador(self,matriz_llena,posicion,mensaje):
            i=posicion[0]
            j=posicion[1]
            posicion_jugador1=[[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador2=[[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador3=[[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador4=[[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador5=[[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador6=[[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador7=[[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador8=[[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            posicion_jugador9=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            if posicion[0]==1 and  posicion[1]==1:
                posicion_jugador=posicion_jugador1
            elif posicion[0]==1 and  posicion[1]==2:
                posicion_jugador=posicion_jugador2
            elif posicion[0]==1 and  posicion[1]==3:
                posicion_jugador=posicion_jugador3
            elif posicion[0]==2 and  posicion[1]==1:
                posicion_jugador=posicion_jugador4
            elif posicion[0]==2 and  posicion[1]==2:
                posicion_jugador=posicion_jugador5
            elif posicion[0]==2 and  posicion[1]==3:
                posicion_jugador=posicion_jugador6
            elif posicion[0]==3 and  posicion[1]==1:
                posicion_jugador=posicion_jugador7
            elif posicion[0]==3 and  posicion[1]==2:
                posicion_jugador=posicion_jugador8
            elif posicion[0]==3 and  posicion[1]==3:
                posicion_jugador=posicion_jugador9
            for i in range(self.fila):
                for j in range(self.columna):
                    pass
                    matriz_llena[i][j]=posicion_jugador[i][j]
            return matriz_llena

        def cargar_enemigo(self,matriz_llena_enemigo,posicion,mensaje):
            i=posicion[0]
            j=posicion[1]
            posicion_enemigo1=[[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo2=[[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo3=[[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo4=[[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo5=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo6=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo7=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo8=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo9=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo10=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo11=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo12=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            posicion_enemigo13=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0]]
            posicion_enemigo14=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0]]
            posicion_enemigo15=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0]]
            posicion_enemigo16=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0]]
            if posicion[0]==3 and posicion[1]==3:
                posicion_enemigo= posicion_enemigo1
            elif posicion[0]==3 and posicion[1]==4:
                posicion_enemigo= posicion_enemigo2
            elif posicion[0]==3 and posicion[1]==5:
                posicion_enemigo= posicion_enemigo3
            elif posicion[0]==3 and posicion[1]==6:
                posicion_enemigo= posicion_enemigo4
            elif posicion[0]==4 and posicion[1]==3:
                posicion_enemigo= posicion_enemigo5
            elif posicion[0]==4 and posicion[1]==4:
                posicion_enemigo= posicion_enemigo6
            elif posicion[0]==4 and posicion[1]==5:
                posicion_enemigo= posicion_enemigo7
            elif posicion[0]==4 and posicion[1]==6:
                posicion_enemigo= posicion_enemigo8
            elif posicion[0]==5 and posicion[1]==3:
                posicion_enemigo= posicion_enemigo9
            elif posicion[0]==5 and posicion[1]==4:
                posicion_enemigo= posicion_enemigo10
            elif posicion[0]==5 and posicion[1]==5:
                posicion_enemigo= posicion_enemigo11
            elif posicion[0]==5 and posicion[1]==6:
                posicion_enemigo= posicion_enemigo12
            elif posicion[0]==6 and posicion[1]==3:
                posicion_enemigo= posicion_enemigo13
            elif posicion[0]==6 and posicion[1]==4:
                posicion_enemigo= posicion_enemigo14
            elif posicion[0]==6 and posicion[1]==5:
                posicion_enemigo= posicion_enemigo15
            elif posicion[0]==6 and posicion[1]==6:
                posicion_enemigo= posicion_enemigo16
            for i in range(self.fila):
                for j in range(self.columna):
                    matriz_llena_enemigo[i][j]=posicion_enemigo[i][j]
            return matriz_llena_enemigo
        def jugador_ataca(self,matriz,memoria):
            bandera=True
            while bandera:
                i=random.randint(0,(jugador1.fila-1))
                j=random.randint(0,(jugador1.columna-1))
                print("disparo hacia : ",self.nombre)
                print("posicion: ",i,j)
                if matriz[i][j]==1 and memoria[i][j]==0:
                    matriz[i][j]=0
                    memoria[i][j]=1
                    self.vida-=5
                    print("meydey")
                    bandera=True
                elif matriz[i][j]==0:
                    bandera=False
                    print("Fallo!!!")
    #objeto jugador 1
    def jugador_1(jugador1,matriz_llena_jugador1):
        posicion=jugador1.posicion()
        jugador1.cargar_jugador(matriz_llena_jugador1,posicion,"posicion del tanke: ")
    #Objeto jugador2
    def jugador_2(jugador2,matriz_llena_jugador2):
        posicion=jugador2.posicion()
        
        jugador2.cargar_jugador(matriz_llena_jugador2,posicion,"posicion del tanke: ")
    #enemigo
    def enemigo_(enemigo,matriz_llena_enemigo):
        posicion=enemigo.posicion()
        enemigo.cargar_enemigo(matriz_llena_enemigo,posicion,"posicion: ")
    #secuencia de ataque
    def dibujar(matrix, top_left, color, border_color):
        filax, columnax = len(matrix), len(matrix[0])
        for i in range(filax):
            for j in range(columnax):
                if matrix[i][j] == 0:
                    pygame.draw.rect(screen, color, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda), 1)
                else:

                    pygame.draw.rect(screen, NEGRO, pygame.Rect(top_left[0] + j*tamaño_celda, top_left[1] + i*tamaño_celda, tamaño_celda, tamaño_celda))
        pygame.draw.rect(screen, border_color, pygame.Rect(top_left[0], top_left[1], columnax*tamaño_celda, filax*tamaño_celda), 3)    
    #algoritmo principal
    bandera=True
    while bandera:
        posicion_fila1=random.randint(0,4)
        posicion_columna1=random.randint(0,4)
        if ((posicion_fila1>0 and posicion_fila1<4) and (posicion_columna1>1 and posicion_columna1<4)):
            bandera=False
    #jugador1
    #fila,columna,vida,posicion_fila,posicion_columna,nombre
    jugador1=area(10,5,30,posicion_fila1,posicion_columna1,"jugador 1")
    matriz_llena_jugador1=jugador1.llenar_matriz()
    memoria_jugador1=jugador1.llenar_matriz()
    jugador_1(jugador1,matriz_llena_jugador1)
    bandera=True
    while bandera:
        posicion_fila2=random.randint(0,4)
        posicion_columna2=random.randint(0,4)
        if ((posicion_fila2>0 and posicion_fila2<4) and (posicion_columna2>1 and posicion_columna2<4)):
            bandera=False
    #jugador2
    #fila,columna,vida,posicion_fila,posicion_columna,nombre
    jugador2=area(10,5,30,posicion_fila2,posicion_columna2,"jugador 2")
    matriz_llena_jugador2=jugador2.llenar_matriz()
    memoria_jugador2=jugador1.llenar_matriz()
    jugador_2(jugador2,matriz_llena_jugador2)
    bandera=True
    while bandera:
        posicion_fila=random.randint(0,9)
        posicion_columna=random.randint(0,9)
        if ((posicion_fila>2 and posicion_fila<7) and (posicion_columna>2 and posicion_columna<7)):
            bandera=False
    #enemigo
    #fila,columna,vida,posicion_fila,posicion_columna,nombre
    enemigo=area(10,10,105,posicion_fila,posicion_columna,"enemigo")
    matriz_llena_enemigo=enemigo.llenar_matriz()
    memoria_enemigo=enemigo.llenar_matriz()
    enemigo_(enemigo,matriz_llena_enemigo)

    pygame.init()
    ANCHO, ALTO = 1100, 600
    screen = pygame.display.set_mode((ANCHO, ALTO))
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)
    CELESTE = (128, 191, 255)
    AMARILLO = (255, 255, 0)
    NEGRO = (0, 0, 0)
    tamaño_celda = 50
    #ataque hacia la maquina
    running=True
    turno_jugador=True
    contador=0
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sound = pygame.mixer.Sound("disparo.mp3")
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.mixer.music.play(-1)
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and turno_jugador:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 50 +   10*tamaño_celda and 50 <= y <= 50 + 10*tamaño_celda:
                        i = (y - 50) // tamaño_celda
                        j = (x - 50) // tamaño_celda
                        sound.play()
                        if (matriz_llena_enemigo[i][j] == 1 and memoria_enemigo[i][j] == 0):
                            memoria_enemigo[i][j] = 1
                            enemigo.vida-=5
                        if jugador1.vida>0 and jugador2.vida>0 and enemigo.vida!=0:
                            contador+=1
                        elif jugador1.vida==0 and jugador2.vida>0 and enemigo.vida!=0:
                            contador=2
                        elif jugador1.vida>0 and jugador2.vida==0 and enemigo.vida!=0:
                            contador=1
                        turno_jugador=False
        if not turno_jugador and contador % 2!=0:
            jugador1.jugador_ataca(matriz_llena_jugador1,memoria_jugador1)
            turno_jugador=True
        elif not turno_jugador and contador % 2==0:
            jugador2.jugador_ataca(matriz_llena_jugador2,memoria_jugador2)
            turno_jugador=True
        elif (jugador1.vida==0 and jugador2.vida==0) or enemigo.vida==0:
            running=False
            play_video("video3.mp4")
            main_menu()
            sys.exit()
        screen.fill(CELESTE)
        font = pygame.font.Font(None, 36)
        text = font.render('Enemigo'+" = "+str(enemigo.vida), 2, (10, 10, 10))
        screen.blit(text, (50, 10))
        dibujar(memoria_enemigo, (50, 50), ROJO, NEGRO)

        text = font.render('Jugador 1'+" = "+str(jugador1.vida), 1, (10, 10, 10))
        screen.blit(text, (50 + 10*tamaño_celda, 10))
        dibujar(matriz_llena_jugador1, (50 + 10*tamaño_celda, 50), VERDE, NEGRO)

        text = font.render('Jugador 2'+" = "+str(jugador2.vida), 1, (10, 10, 10))
        screen.blit(text, (50 + 15*tamaño_celda, 10))
        dibujar(matriz_llena_jugador2, (50 + 15*tamaño_celda, 50), AZUL, NEGRO)
        pygame.display.flip()
    pygame.quit()

# Función para mostrar los créditos
def credits():
    play_video("video3.mp4")

if __name__ == "__main__":
    main_menu()
