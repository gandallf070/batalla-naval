#jeugo-poo
import random
import pygame
import random
import time
import sys
import numpy as np
import cv2
from pygame.locals import *

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
        # print(mensaje+self.nombre)
        # print(posicion)
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
        # print(mensaje,enemigo.nombre)
        # print(posicion)
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

def jugador_ataca():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 50 +   10*tamaño_celda and 50 <= y <= 50 + 10*tamaño_celda:
                    i = (y - 50) // tamaño_celda
                    j = (x - 50) // tamaño_celda
                    if (matriz_llena_enemigo[i][j] == 1 and memoria_enemigo[i][j] == 0):
                        memoria_enemigo[i][j] = 1
                        enemigo.vida-=5
                        print("posicion: ",i,j)
    
def enemigo_ataca(matriz):
        i=random.randint(0,(jugador1.fila-1))
        j=random.randint(0,(jugador1.columna-1))
        print("Maquina ataca posicion: ",i,j)
        if matriz[i][j]==1:
            matriz[i][j]=0
            jugador1.vida-=5  

def turno():
    pass

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
#ataca solamente 1 vez.,..hasta crear turnos
enemigo_ataca(matriz_llena_jugador1)
enemigo_ataca(matriz_llena_jugador2)
#ataque hacia la maquina
running=True
while running:
    if enemigo.vida==0:
        break      
    else:
        if jugador1.vida==100000  and jugador2.vida==1000000:
            enemigo_ataca(matriz_llena_jugador1)
            enemigo_ataca(matriz_llena_jugador2)
        jugador_ataca()
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
background_image = pygame.image.load("batalla-2.jpg").convert()
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

# Variable para indicar si el juego está activo
juego_activo = False
acerca_de_abierto = False

# Fondo para la ventana "Acerca de"
fondo_acerca_de = pygame.Surface((400, 200))
fondo_acerca_de.fill((255, 255, 255))

clock = pygame.time.Clock()

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

def iniciar_juego():
    global cap, juego_activo
    juego_activo = True
    pygame.mixer.music.play(-1)
    while juego_activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_activo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                manejar_clic(event.pos)
            elif event.type == pygame.KEYDOWN:
                manejar_teclado(event.key)

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out_frame = pygame.surfarray.make_surface(np.transpose(frame_rgb, (1, 0, 2)))

        screen.blit(out_frame, (0, 0))
        pygame.display.flip()
        clock.tick(fps)

    cap.release()
    pygame.mixer.music.stop()

def manejar_teclado(tecla):
    global MENU_SELECCION
    if tecla == pygame.K_UP:
        MENU_SELECCION = (MENU_SELECCION - 1) % len(MENU_OPCIONES)
    elif tecla == pygame.K_DOWN:
        MENU_SELECCION = (MENU_SELECCION + 1) % len(MENU_OPCIONES)
    elif tecla == pygame.K_RETURN or tecla == 13:  # Añadido 13 para Enter
        manejar_clic()
    elif tecla == pygame.K_ESCAPE:
        salir()

def manejar_clic(posicion=None):
    global juego_activo, acerca_de_abierto
    x, y = posicion if posicion else pygame.mouse.get_pos()
    for i, opcion in enumerate(MENU_OPCIONES):
        x_opcion = ANCHO // 2
        y_opcion = ALTO // 2 + i * 50
        ancho_opcion = 200
        alto_opcion = 40
        if x_opcion - ancho_opcion // 2 < x < x_opcion + ancho_opcion // 2 and \
           y_opcion - alto_opcion // 2 < y < y_opcion + alto_opcion // 2:
            if i == 0:
                iniciar_juego()
            elif i == 1:
                acerca_de()
            elif i == 2:
                salir()
            return  # Agrega esta línea para evitar la ejecución de otras opciones cuando se hace clic en un botón

def acerca_de():
    global acerca_de_abierto
    acerca_de_abierto = True
    while acerca_de_abierto:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                acerca_de_abierto = False
        pantalla.blit(fondo_acerca_de, (ANCHO // 2 - 200, ALTO // 2 - 100))
        # nombres_texto = pygame.font.SysFont(None, 24).render("Edward Camargo Marca \n Pavel Tango Sánchez", True, NEGRO)
        # pantalla.blit(nombres_texto, (ANCHO // 2 - 190, ALTO // 2 - 90))
        nombres = "Edward Camargo Marca \nPavel Tango Sánchez"
        nombres_lineas = nombres.splitlines()

        for i, linea in enumerate(nombres_lineas):
            texto = pygame.font.SysFont(None, 24).render(linea, True, NEGRO)
            pantalla.blit(texto, (ANCHO // 2 - 190, ALTO // 2 - 90 + i * 30))
        pygame.display.flip()

#     fondo_acerca_de = pygame.image.load("ruta/a/tu/fondo.png")
#     pantalla_acerca_de = pygame.display.set_mode((ANCHO, ALTO))
#     pantalla_acerca_de.blit(fondo_acerca_de, (0, 0))

#     nombres = "Edward Camargo Marca \n Pavel Tango Sánchez"
#     nombres_lineas = nombres.splitlines()

# for i, linea in enumerate(nombres_lineas):
#     texto = pygame.font.SysFont(None, 24).render(linea, True, NEGRO)
#     pantalla_acerca_de.blit(texto, (ANCHO // 2 - 190, ALTO // 2 - 90 + i * 30))

pygame.display.flip()


def salir():
    pygame.quit()
    sys.exit()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            manejar_teclado(evento.key)
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            manejar_clic(evento.pos)

    dibujar_menu()
