#INTEGRANTES:
# 17635859-9 Gabriela Sepulveda Bravo
# 19488642-k Gaspar Correa Vergara
# 19399143-2 Julio Rojas Cantillanez
import pygame, sys
from pygame.locals import *
from random import choice, randint
from configuracion import *
from constantes import *
from utilidades import *

vidascpu=[0,1,2,3,4,5]
vidasmias=[0,1,2,3,4,5]
def completar_tablero (cursor, tablero, barco, sentido):
    barquitos2=[BARCO1,BARCO2,BARCO3,BARCO4,BARCO5]
    
    i=0
    j=0
    if cursor[0][0]>200 and cursor[0][0]<233:
        j=0
    elif cursor[0][0]>233 and cursor[0][0]<266:
        j=1
    elif cursor[0][0]>266 and cursor[0][0]<299:
        j=2
    elif cursor[0][0]>299 and cursor[0][0]<332:
        j=3
    elif cursor[0][0]>332 and cursor[0][0]<365:
        j=4
    elif cursor[0][0]>365 and cursor[0][0]<398:
        j=5
    elif cursor[0][0]>398 and cursor[0][0]<431:
        j=6
    elif cursor[0][0]>431 and cursor[0][0]<464:
        j=7
    elif cursor[0][0]>464 and cursor[0][0]<497:
        j=8
    elif cursor[0][0]>497 and cursor[0][0]<530:
        j=9
    else:
        return (-1,-1)
    if cursor[0][1]>50 and cursor[0][1]<83:
        i=0
    elif cursor[0][1]>83 and cursor[0][1]<116:
        i=1
    elif cursor[0][1]>116 and cursor[0][1]<149:
        i=2
    elif cursor[0][1]>149 and cursor[0][1]<182:
        i=3
    elif cursor[0][1]>182 and cursor[0][1]<215:
        i=4
    elif cursor[0][1]>215 and cursor[0][1]<248:
        i=5
    elif cursor[0][1]>248 and cursor[0][1]<281:
        i=6
    elif cursor[0][1]>281 and cursor[0][1]<314:
        i=7
    elif cursor[0][1]>314 and cursor[0][1]<347:
        i=8
    elif cursor[0][1]>347 and cursor[0][1]<380:
        i=9
    else:
        return (-1,-1)
    if sentido==NORTE:
        if i+barco-1>=10:
            return (-1,-1)
    else:
        if j+barco-1>=10:
            return (-1,-1)
    for e in range(barco):
        if sentido==NORTE:
            if tablero[i+e][j]!=0:
                return (-1,-1)
        else:
            if tablero[i][j+e]!=0:
                return (-1,-1)
    for e in range(barco):
        if sentido==NORTE:
            tablero[i+e][j]=barquitos2[barco-1]
        else:
            tablero[i][j+e]=barquitos2[barco-1]
        
    return (i,j)

def actualizar_info_posicion (fila, columna, barco_actual):
    if fila!=-1 and columna!=-1:
        barquitos=["A","B","C","D","E"]
        INFO_BARCOS[barquitos[barco_actual-1]][0][0]=0
        return True
    else:
        return False
    

def posicionar_barcos_enemigos(t):
    barquitos=[BARCO1,BARCO2,BARCO3,BARCO4,BARCO5]
    c=1
    while c<6:
        error=0
        i=randint(0,9)
        j=randint(0,9)
        sentido=[NORTE,OESTE]
        z=choice(sentido)
        if NORTE==z:
            if i+c<10:
                for e in range(c):
                    if t[i+e][j]!=0:
                        error=1
                if error!=1:
                    for e in range(c):
                        t[i+e][j]=barquitos[c-1]
                        
            else:
                error=1
        else:
            if j+c<10:
                for e in range(c):
                    if t[i][j+e]!=0:
                        error=1
                if error!=1:
                    for e in range(c):
                        t[i][j+e]=barquitos[c-1]
                        
            else:
                error=1
        if error!=1:
            c=c+1
        
    
    
    return None
    
def procesar_disparo(cursor, tablero, tablero2, dx, dy):
    i=0
    j=0
    barquitos=[0,5,4,3,2,1]
    if cursor[0][0]>430 and cursor[0][0]<463:
        j=0
    elif cursor[0][0]>463 and cursor[0][0]<496:
        j=1
    elif cursor[0][0]>496 and cursor[0][0]<529:
        j=2
    elif cursor[0][0]>529 and cursor[0][0]<562:
        j=3
    elif cursor[0][0]>562 and cursor[0][0]<595:
        j=4
    elif cursor[0][0]>595 and cursor[0][0]<628:
        j=5
    elif cursor[0][0]>628 and cursor[0][0]<661:
        j=6
    elif cursor[0][0]>661 and cursor[0][0]<694:
        j=7
    elif cursor[0][0]>694 and cursor[0][0]<727:
        j=8
    elif cursor[0][0]>727 and cursor[0][0]<760:
        j=9
    else:
        return [-1,(-1,-1)]
    if cursor[0][1]>30 and cursor[0][1]<63:
        i=0
    elif cursor[0][1]>63 and cursor[0][1]<96:
        i=1
    elif cursor[0][1]>96 and cursor[0][1]<129:
        i=2
    elif cursor[0][1]>129 and cursor[0][1]<162:
        i=3
    elif cursor[0][1]>162 and cursor[0][1]<195:
        i=4
    elif cursor[0][1]>195 and cursor[0][1]<228:
        i=5
    elif cursor[0][1]>228 and cursor[0][1]<261:
        i=6
    elif cursor[0][1]>261 and cursor[0][1]<294:
        i=7
    elif cursor[0][1]>294 and cursor[0][1]<327:
        i=8
    elif cursor[0][1]>327 and cursor[0][1]<360:
        i=9
    else:
        return [-1,(-1,-1)]
    tablero2[i][j]=barquitos[tablero[i][j]]+10
    return [barquitos[tablero[i][j]],(i,j)] 

def disparo_enemigo(tablero, tablero2):
    while True:
        i=randint(0,9)
        j=randint(0,9)
        if tablero[i][j]!=-9 and tablero[i][j]!=9:
            break
    barquitos=[0,5,4,3,2,1]
    barco=tablero[i][j]
    tablero2[i][j]=barquitos[tablero[i][j]]+10
    
    return [barquitos[barco],(i,j)]


def actualizar_tablero(info_disparos, disparos, jugada):
    barquitos=["A","B","C","D","E"]
    acierto=[1,2,3,4,5]
    i,j=disparos[1]
    if info_disparos[i][j]-10 in acierto:
        info_disparos[i][j]=9
    else:
        info_disparos[i][j]=-9
    
    if jugada%2==0:
        if disparos[0]!=0:
            vidascpu[disparos[0]]=vidascpu[disparos[0]]-1
            if vidascpu[disparos[0]]==0:
                INFO_BARCOS[barquitos[disparos[0]-1]][0][0]=0
                return 1
            else:
                return 0
    else:
        if disparos[0]!=0:
            vidasmias[disparos[0]]=vidasmias[disparos[0]]-1
            if vidasmias[disparos[0]]==0:
                return 1
            else:
                return 0    

