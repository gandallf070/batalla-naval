import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
width, height = 1100, 600
screen = pygame.display.set_mode((width, height))

# Definir colores
WHITE = (12,183,242)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Definir matrices
enemigo = [[0]*10 for _ in range(10)]
jugador1 = [[0]*5 for _ in range(10)]
jugador2 = [[0]*5 for _ in range(10)]

# Definir tamaño de las celdas
cell_size = 50

# Dibujar matrices
def draw_matrix(matrix, top_left, color, border_color):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                pygame.draw.rect(screen, color, pygame.Rect(top_left[0] + j*cell_size, top_left[1] + i*cell_size, cell_size, cell_size), 1)
            else:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(top_left[0] + j*cell_size, top_left[1] + i*cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, border_color, pygame.Rect(top_left[0], top_left[1], cols*cell_size, rows*cell_size), 3)

# Cambiar aleatoriamente una celda de una matriz
def random_change(matrix):
    rows, cols = len(matrix), len(matrix[0])
    i = random.randint(0, rows - 1)
    j = random.randint(0, cols - 1)
    matrix[i][j] = 1

# Bucle principal
running = True
random_change(jugador1)
random_change(jugador2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 50 <= x <= 50 + 10*cell_size and 50 <= y <= 50 + 10*cell_size:
                i = (y - 50) // cell_size
                j = (x - 50) // cell_size
                if enemigo[i][j] == 0:
                    enemigo[i][j] = 1
                    print(f'Has hecho clic en la celda ({i}, {j}) de la matriz "enemigo".')

    screen.fill(WHITE)

    font = pygame.font.Font(None, 36)
    text = font.render('Enemigo', 1, (10, 10, 10))
    screen.blit(text, (50, 10))
    draw_matrix(enemigo, (50, 50), RED, BLACK)

    text = font.render('Jugador 1', 1, (10, 10, 10))
    screen.blit(text, (50 + 10*cell_size, 10))
    draw_matrix(jugador1, (50 + 10*cell_size, 50), GREEN, BLACK)

    text = font.render('Jugador 2', 1, (10, 10, 10))
    screen.blit(text, (50 + 15*cell_size, 10))
    draw_matrix(jugador2, (50 + 15*cell_size, 50), BLUE, BLACK)

    pygame.display.flip()

# pygame.quit()
#jeugo-poo
# import random
# import time

# class Area():
#     def __init__(self, n, m, vida, posicion_fila, posicion_columna, nombre):
#         self.nombre = nombre
#         self.fila = n
#         self.columna = m
#         self.vida = vida
#         self.posicion_fila = posicion_fila
#         self.posicion_columna = posicion_columna

#     def posicion(self):
#         return [self.posicion_fila, self.posicion_columna]

#     def llenar_matriz(self):
#         return [[0]*self.columna for _ in range(self.fila)]

#     def mostrar(self, matriz_llena):
#         for i in range(self.fila):
#             for j in range(self.columna):
#                 print(matriz_llena[i][j], end="  ")
#             print("")

#     def cargar_jugador(self, matriz_llena, posicion, mensaje):
#         # Código para cargar al jugador...
#         i=posicion[0]
#         j=posicion[1]
#         posicion_jugador1=[[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador2=[[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador3=[[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador4=[[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador5=[[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador6=[[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador7=[[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador8=[[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         posicion_jugador9=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,1],[0,0,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#         if posicion[0]==1 and  posicion[1]==1:
#             posicion_jugador=posicion_jugador1
#         elif posicion[0]==1 and  posicion[1]==2:
#             posicion_jugador=posicion_jugador2
#         elif posicion[0]==1 and  posicion[1]==3:
#             posicion_jugador=posicion_jugador3
#         elif posicion[0]==2 and  posicion[1]==1:
#             posicion_jugador=posicion_jugador4
#         elif posicion[0]==2 and  posicion[1]==2:
#             posicion_jugador=posicion_jugador5
#         elif posicion[0]==2 and  posicion[1]==3:
#             posicion_jugador=posicion_jugador6
#         elif posicion[0]==3 and  posicion[1]==1:
#             posicion_jugador=posicion_jugador7
#         elif posicion[0]==3 and  posicion[1]==2:
#             posicion_jugador=posicion_jugador8
#         elif posicion[0]==3 and  posicion[1]==3:
#             posicion_jugador=posicion_jugador9
#         for i in range(self.fila):
#             for j in range(self.columna):
#                 pass
#                 matriz_llena[i][j]=posicion_jugador[i][j]
#         return matriz_llena

#     def cargar_enemigo(self, matriz_llena, posicion, mensaje):
#         # Código para cargar al enemigo...
#         i=posicion[0]
#         j=posicion[1]
#         posicion_enemigo1=[[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo2=[[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo3=[[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo4=[[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo5=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo6=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo7=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo8=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo9=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo10=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo11=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo12=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#         posicion_enemigo13=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0]]
#         posicion_enemigo14=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0,0]]
#         posicion_enemigo15=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0,0,0]]
#         posicion_enemigo16=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0]]
#         if posicion[0]==3 and posicion[1]==3:
#             posicion_enemigo= posicion_enemigo1
#         elif posicion[0]==3 and posicion[1]==4:
#             posicion_enemigo= posicion_enemigo2
#         elif posicion[0]==3 and posicion[1]==5:
#             posicion_enemigo= posicion_enemigo3
#         elif posicion[0]==3 and posicion[1]==6:
#             posicion_enemigo= posicion_enemigo4
#         elif posicion[0]==4 and posicion[1]==3:
#             posicion_enemigo= posicion_enemigo5
#         elif posicion[0]==4 and posicion[1]==4:
#             posicion_enemigo= posicion_enemigo6
#         elif posicion[0]==4 and posicion[1]==5:
#             posicion_enemigo= posicion_enemigo7
#         elif posicion[0]==4 and posicion[1]==6:
#             posicion_enemigo= posicion_enemigo8
#         elif posicion[0]==5 and posicion[1]==3:
#             posicion_enemigo= posicion_enemigo9
#         elif posicion[0]==5 and posicion[1]==4:
#             posicion_enemigo= posicion_enemigo10
#         elif posicion[0]==5 and posicion[1]==5:
#             posicion_enemigo= posicion_enemigo11
#         elif posicion[0]==5 and posicion[1]==6:
#             posicion_enemigo= posicion_enemigo12
#         elif posicion[0]==6 and posicion[1]==3:
#             posicion_enemigo= posicion_enemigo13
#         elif posicion[0]==6 and posicion[1]==4:
#             posicion_enemigo= posicion_enemigo14
#         elif posicion[0]==6 and posicion[1]==5:
#             posicion_enemigo= posicion_enemigo15
#         elif posicion[0]==6 and posicion[1]==6:
#             posicion_enemigo= posicion_enemigo16
#         for i in range(self.fila):
#             for j in range(self.columna):
#                 matriz_llena_enemigo[i][j]=posicion_enemigo[i][j]
#         return matriz_llena_enemigo

#     def atacar(self, matriz_llena, memoria):
#         # Código para atacar...
#         bandera=True
#         bandera1=True
#         contador=0
#         print(self.nombre)
#         # self.mostrar(matriz_llena)
#         # print("memoria",self.nombre)
#         # self.mostrar(memoria)
#         while bandera:
#             while bandera1:
#                 #posicion "i" , "j"
#                 i=random.randint(0,(self.fila-1))
#                 j=random.randint(0,(self.columna-1))
#                 print(i," ",j)
#                 #memoria jugador
#                 if (memoria[i][j]==0):
#                     memoria[i][j]=1
#                     bandera1=False
#             contador+=1
#             if (matriz_llena[i][j]==1):
#                 print("se me fue mi amigo bronco ")
#                 (self.vida)-=5
#                 #aux=matriz_llena[i][j]
#                 matriz_llena[i][j]=0
#             else:
#                 print("uff... casi!")
#                 bandera=False
#                 #aux=0
#             # if (aux==0):
#             # # if (jugador1.vida<0 and jugador2.vida<0) or (enemigo.vida<0):
#             #         bandera=False
#             print(contador, " disparo ")

# def jugador_1(jugador1, matriz_llena_jugador1):
#     posicion = jugador1.posicion()
#     jugador1.cargar_jugador(matriz_llena_jugador1, posicion, "posicion del tanque: ")

# def jugador_2(jugador2, matriz_llena_jugador2):
#     posicion = jugador2.posicion()
#     jugador2.cargar_jugador(matriz_llena_jugador2, posicion, "posicion del tanque: ")

# def enemigo_(enemigo, matriz_llena_enemigo):
#     posicion = enemigo.posicion()
#     enemigo.cargar_enemigo(matriz_llena_enemigo, posicion, "posicion: ")

# # Código principal...
# bandera=True
# while bandera:
#     posicion_fila1=random.randint(0,4)
#     posicion_columna1=random.randint(0,4)
#     if ((posicion_fila1>0 and posicion_fila1<4) and (posicion_columna1>1 and posicion_columna1<4)):
#         bandera=False
# #jugador1
# #fila,columna,vida,posicion_fila,posicion_columna,nombre
# jugador1=Area(10,5,30,posicion_fila1,posicion_columna1,"jugador 1")
# matriz_llena_jugador1=jugador1.llenar_matriz()
# memoria_jugador1=jugador1.llenar_matriz()
# jugador_1(jugador1,matriz_llena_jugador1)
# bandera=True
# while bandera:
#     posicion_fila2=random.randint(0,4)
#     posicion_columna2=random.randint(0,4)
#     if ((posicion_fila2>0 and posicion_fila2<4) and (posicion_columna2>1 and posicion_columna2<4)):
#         bandera=False
# #jugador2
# #fila,columna,vida,posicion_fila,posicion_columna,nombre
# jugador2=Area(10,5,30,posicion_fila2,posicion_columna2,"jugador 2")
# matriz_llena_jugador2=jugador2.llenar_matriz()
# memoria_jugador2=jugador1.llenar_matriz()
# jugador_2(jugador2,matriz_llena_jugador2)
# bandera=True
# while bandera:
#     posicion_fila=random.randint(0,9)
#     posicion_columna=random.randint(0,9)
#     if ((posicion_fila>2 and posicion_fila<7) and (posicion_columna>2 and posicion_columna<7)):
#         bandera=False

# def turno(jugador1, jugador2, enemigo):
#     bandera = True
#     while bandera:
#         if jugador1.vida > 0 and jugador2.vida > 0 and enemigo.vida > 0:
#             jugador1.atacar(matriz_llena_jugador1, memoria_jugador1)
#             print(jugador1.vida, jugador1.nombre)
#             time.sleep(3)
#             enemigo.atacar(matriz_llena_enemigo, memoria_enemigo)
#             print(enemigo.vida, enemigo.nombre)
#             time.sleep(3)
#             jugador2.atacar(matriz_llena_jugador2, memoria_jugador2)
#             print(jugador2.vida, jugador2.nombre)
#             time.sleep(3)
#             enemigo.atacar(matriz_llena_enemigo, memoria_enemigo)
#             print(enemigo.vida, enemigo.nombre)
#             time.sleep(3)
#         elif jugador1.vida > 0 and jugador2.vida == 0 and enemigo.vida > 0:
#             jugador1.atacar(matriz_llena_jugador1, memoria_jugador1)
#             print(jugador1.vida, jugador1.nombre)
#             time.sleep(3)
#             enemigo.atacar(matriz_llena_enemigo, memoria_enemigo)
#             print(enemigo.vida, enemigo.nombre)
#             time.sleep(3)
#         elif jugador1.vida == 0 and jugador2.vida > 0 and enemigo.vida > 0:
#             jugador2.atacar(matriz_llena_jugador2, memoria_jugador2)
#             print(jugador2.vida, jugador2.nombre)
#             time.sleep(3)
#             enemigo.atacar(matriz_llena_enemigo, memoria_enemigo)
#             print(enemigo.vida, enemigo.nombre)
#             time.sleep(3)
#         elif (jugador1.vida > 0 or jugador2.vida > 0) and enemigo.vida == 0:
#             print(jugador1.vida, jugador1.nombre)
#             print(jugador2.vida, jugador2.nombre)
#             print(enemigo.vida, enemigo.nombre)
#             bandera = False
#         elif (jugador1.vida == 0 and jugador2.vida == 0) and enemigo.vida > 0:
#             print(jugador1.vida, jugador1.nombre)
#             print(jugador2.vida, jugador2.nombre)
#             print(enemigo.vida, enemigo.nombre)
#             bandera = False

# #fila,columna,vida,posicion_fila,posicion_columna,nombre
# enemigo=Area(10,10,80,posicion_fila,posicion_columna,"enemigo")
# matriz_llena_enemigo=enemigo.llenar_matriz()
# memoria_enemigo=enemigo.llenar_matriz()
# enemigo_(enemigo,matriz_llena_enemigo)

# turno(jugador1,jugador2,enemigo)