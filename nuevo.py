#jeugo-poo
import random
import pygame
import random
import time
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
def enemigo_ataca():
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
                        print("WHILE")
    
def jugador_ataca(matriz):
        i=random.randint(0,(jugador1.fila-1))
        j=random.randint(0,(jugador1.columna-1))
        print("posicion: ",i,j)
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
jugador_ataca(matriz_llena_jugador1)
jugador_ataca(matriz_llena_jugador2)
#ataque hacia la maquina
running=True
while running:
    if enemigo.vida==0:
        break      
    else:
        enemigo_ataca()
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

