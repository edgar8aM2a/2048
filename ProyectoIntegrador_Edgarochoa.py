"""
Edgar Adolfo Ochoa Mendoza A00344644
Avanze de reto para pensamiento computacional
"2048"
9/10/2020
"""
from copy import deepcopy
from random import *
import tkinter

#funciones

#crear tablero
def crear_tablero():
    tablero=[[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    return tablero


def encontrar_ceros(m): #esta Funcion te regresa una lista con los indices de las casillas donde existe un cero
    ceros=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==0:
               ceros.append([i,j])
               
    return ceros

def generar_numero(m): 
    numero_aleatorio=choices([2,4],[9,1],k=1) #Elige un 2 0 4 aleatoriamente con la probabilidad 9 a 1
    posicion=choice(encontrar_ceros(m)) #usa la funcion encontrar ceros para ver donde puede insertarlo y escoge una posicion aleatoriamente 
    m[posicion[0]][posicion[1]]=numero_aleatorio[0] #Coloca el numero aleatorio en la posicion aleatoria 
    return m
#D
def desplazar_derecha(m): # desplaza los numero a la derecha
    ya_sumados=[]
    posibilidades=False
    for t in range(3):
        for i in range(len(m)):
            for j in range(-2,-len(m[i])-1,-1):
                if m[i][j]!=0 and m[i][j+1]==0: #caso1 solo hay ceros en el camino
                    m[i][j+1]= m[i][j]
                    m[i][j]=0
                    posibilidades=True
                        
                elif m[i][j]==m[i][j+1] and [i,j] not in ya_sumados and m[i][j]!=0:#caso2 hay un numero igual en el camino
                    m[i][j+1]+=m[i][j]
                    ya_sumados.append([i,j+1])
                    ya_sumados.append([i,j])
                    m[i][j]=0
                    posibilidades=True
                                    
    if posibilidades==True:
        generar_numero(m)
    return m
#A
def desplazar_izquierda(m): # desplaza los numero a la izquierda
    ya_sumados=[]
    posibilidades=False
    for t in range(3):
        for i in range(len(m)):
            for j in range(1,len(m[i])):
                if m[i][j]!=0 and m[i][j-1]==0: #caso1 solo hay ceros en el camino
                    m[i][j-1]= m[i][j]
                    m[i][j]=0
                    posibilidades=True
                    
                elif m[i][j]==m[i][j-1] and [i,j] not in ya_sumados and m[i][j]!=0:#caso2 hay un numero igual en el camino
                    m[i][j-1]+=m[i][j]
                    ya_sumados.append([i,j-1])
                    ya_sumados.append([i,j])
                    m[i][j]=0
                    posibilidades=True
                    
    if posibilidades==True:
        generar_numero(m)
    return m

#w
def desplazar_arriba(m): # desplaza los numero  hacia arriba
    ya_sumados=[]
    posibilidades=False
    for t in range(3):
        for j in range(len(m)):
            for i in range(1,len(m[j])):
                if m[i][j]!=0 and m[i-1][j]==0: #caso1 solo hay ceros en el camino
                    m[i-1][j]= m[i][j]
                    m[i][j]=0
                    posibilidades=True
                        
                elif m[i][j]==m[i-1][j] and [i,j] not in ya_sumados and m[i][j]!=0:#caso2 hay un numero igual en el camino
                    m[i-1][j]+=m[i][j]
                    ya_sumados.append([i-1,j])
                    ya_sumados.append([i,j])
                    m[i][j]=0
                    posibilidades=True
         
                    
    if posibilidades==True:
        generar_numero(m)
    return m

#Dezplazar abajo s
def desplazar_abajo(m):
    ya_sumados=[]
    posibilidades=False
    for t in range(3):
        for j in range(len(m)):
            for i in range(-2,-len(m[j])-1,-1):
                if m[i][j]!=0 and m[i+1][j]==0: #caso1 solo hay ceros en el camino
                    m[i+1][j]= m[i][j]
                    m[i][j]=0
                    posibilidades=True
                    
                elif m[i][j]==m[i+1][j] and [i,j] not in ya_sumados and m[i][j]!=0:#caso2 hay un numero igual en el camino
                    m[i+1][j]+=m[i][j]
                    ya_sumados.append([i+1,j])
                    ya_sumados.append([i,j])
                    m[i][j]=0
                    posibilidades=True
                    
    if posibilidades==True:
        generar_numero(m)
    return m

#ganador
def ganador(m): # evalua si ya ganaste
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==2048:
                imprimir_tablero(m)
                print("felicidades ganaste")
                return True
#movimientos restantes
def buscar_movimientos(m):#regresa verdadero o falso si es que quedan movientos posibles
    movimiento=False
    for i in range(len(m)):       #horizontal
        for j in range(len(m[i])-1):
            if m[i][j]==m[i][j+1]:
                movimiento=True
    
    for j in range(len(m)):       #Vertical
        for i in range(len(m[j])-1):
            if m[i][j]==m[i+1][j]:
                movimiento=True
    return movimiento

def imprimir_tablero(m): #imprime el tablero
    t=deepcopy(m)
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j]==0:
                t[i][j]=" "       
    for elemento in t:
        print(f"|{elemento[0]:5}|{elemento[1]:5}|{elemento[2]:5}|{elemento[3]:5}|")

#Programa principal
tab=crear_tablero()
generar_numero(tab)
generar_numero(tab)

def calcula_maxmov(m):
    mayor=0
    for i in m:
        for j in i:
            if j>mayor:
                mayor=j
    return mayor

def guarda_score(m):#guarda el score de la partida
    mayor=calcula_maxmov(m)
    lista=[]
    resultado=" "
    with open("score.csv","r") as marcador:
        header=marcador.readline()
        for renglon in marcador:
            lista.append(renglon.strip().split(","))
    topscore=lista[0]
    topscore=int(topscore[0])
    if mayor>topscore:
        topscore=mayor
    resultados=(str(topscore)+","+str(mayor)+"\n")
  
    with open("score.csv","w") as marcador:
        marcador.write(header)
        marcador.write(resultados)
    print("Top score\tTu score")
    print(f"{topscore}{mayor:20}")

    
    
    
print("""
 Mezcla los  numeros para crear un 2048"
 Utiliza las teclas para jugar
                 W▲
            ◄A         D►          
                 S▼              
""")


while True:
    imprimir_tablero(tab)
    print()
    mov=(input("Movimiento: ")).lower()
    
    if mov=="d":
        desplazar_derecha(tab)
    elif mov=="a":
        desplazar_izquierda(tab)
    elif mov=="w":
        desplazar_arriba(tab)
    elif mov=="s":
        desplazar_abajo(tab)
    else:
        print("Tecla incorrecta")
        
        
    if ganador(tab)==True:
        guarda_score(tab)
        break
    if encontrar_ceros(tab)==[]:
        if buscar_movimientos(tab)==False:#perdiste
             imprimir_tablero(tab)
             guarda_score(tab)
             print("No hay mas movimientos perdiste :(")
             break
    
        
    