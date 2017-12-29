#INTEGRANTES
#17635859-9    Gabriela Sepúlveda Bravo
#19487651-3    Pablo Stevens Lagos
#19631883-6    Beatriz Segura Pasten

from turtle import *
import random
shape('turtle')
screensize(620,620)
setup (650,650)

#Funciones construccion tablero
def tableft(left):
    return(left(90), forward(40), left(90), forward(120))
def tabright(right):
    return(right(90), forward(40), right(90), forward(120))
def cuadrado(right,left):
    return (right(90), forward(160),left(90),forward(160),left(90),forward(160),left(90),forward(160))
def pista(right,left):
    return begin_fill(), left(90), forward(80), left(90),forward(40), left(90), forward(80),left(90), forward(40),left(90), forward(80),left(90), forward(40),end_fill(),begin_fill(),left(90), forward(40),right(90),forward(160),right(90), forward(40),right(90), forward(160),right(90), forward(40),right(90), forward(160),end_fill(),begin_fill(),left(90), forward(40),right(135), forward(85),right(90), forward(85),right(135), forward(80),end_fill()

#Construccion del tablero
up()
speed(0)
goto(140,-100)
down()
color('blue')
begin_fill()
cuadrado(right,left)
end_fill()
up()
goto(-100,-300)
down()
color('yellow')
begin_fill()
cuadrado(right,left)
end_fill()
up()
goto(-300,260)
down()
color('red')
begin_fill()
cuadrado(right,left)
end_fill()
up()
goto(260,140)
down()
color('green')
begin_fill()
cuadrado(right,left)
end_fill()
up()
goto(260,-60)
down()
color('blue')
pista(right,left)
up()
goto(-60,-260)
down()
color('yellow')
pista(right,left)
up()
goto(-260,60)
down()
color('red')
pista(right,left)
up()
goto(60,260)
down()
color('green')
pista(right,left)
up()
color('black')
speed(0)
goto(-60,60)
down()
goto(60,-60)
seth(90)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(120)
goto(-60,-60)
seth(180)
forward(240)
right(90)
forward(40)
right(90)
forward(240)
left(90)
forward(40)
left(90)
forward(240)
right(90)
forward(40)
right(90)
forward(600)
right(90)
forward(40)
right(90)
forward(240)
left(90)
forward(40)
left(90)
forward(240)
right(90)
forward(40)
right(90)
forward(240)
left(90)
forward(240)
right(90)
forward(40)
right(90)
forward(240)
left(90)
forward(40)
left(90)
forward(240)
right(90)
forward(40)
right(90)
forward(600)
right(90)
forward(40)
right(90)
forward(240)
left(90)
forward(40)
left(90)
forward(240)
right(90)
forward(40)
right(90)
forward(240)
right(90)
forward(360)
left(90)
forward(120)
tableft(left)
tabright(right)
tableft(left)
tabright(right)
tableft(left)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(120)
tableft(left)
tabright(right)
tableft(left)
tabright(right)
tableft(left)
left(90)
forward(400)
left(90)
forward(120)
tabright(right)
tableft(left)
tabright(right)
tableft(left)
tabright(right)
right (90)
forward(240)
right(90)
forward(160)
left(90)
forward(120)
tabright(right)
tableft(left)
tabright(right)
tableft(left)
tabright(right)
up()
goto(300,-100)
down()
cuadrado(right,left)
up()
goto(-260,-300)
down()
cuadrado(right,left)   
up()
goto(-140,260)
down()
cuadrado(right,left)
up()
goto(100,140)
down()
cuadrado(right,left)
up()
seth(180)
goto(0,0)
hideturtle()

#Jugadores
j1=Turtle()
j2=Turtle()
j3=Turtle()
j4=Turtle()
def Jugador1(j1):
    j1.shape('turtle')
    j1.color('black','red')
    j1.up()
    j1.setheading(270)
    j1.goto(-280,80)
def Jugador2(j2):
    j2.shape('circle')
    j2.color('black','blue')
    j2.up()
    j2.setheading(90)
    j2.goto(280,-80)
def Jugador3(j3):
    j3.shape('square')
    j3.color('black','yellow')
    j3.up()
    j3.setheading(0)
    j3.goto(-80,-280)
def Jugador4(j4):
    j4.shape('triangle')
    j4.color('black','green')
    j4.setheading(180)
    j4.up()
    j4.goto(80,280)
    
#Posicionamiento jugadores
def iniciar_juego(n):
    while n>4 or n<2:
        print 'Numero de jugadores invalido.'
        n=int(raw_input('Ingresa cantidad de jugadores [2 a 4 jugadores]: '))
    print 'Se ingresaron', n, 'jugadores.'
    if n==2:
        Jugador1(j1), Jugador2(j2)
        j3.hideturtle(), j4.hideturtle()
    elif n==3:
        Jugador1(j1), Jugador2(j2), Jugador3(j3)
        j4.hideturtle()
    elif n==4:
        Jugador1(j1), Jugador2(j2), Jugador3(j3), Jugador4(j4)

#Dado
def lanzar_dado(i):
    if i==1:
        a=raw_input('Jugador 1 presione L para lanzar dado: ')
    elif i==2:
        a=raw_input('Jugador 2 presione L para lanzar dado: ')
    elif i==3:
        a=raw_input('Jugador 3 presione L para lanzar dado: ')
    elif i==4:
        a=raw_input('Jugador 4 presione L para lanzar dado: ')
    while a!='L' and a!='l':
        print 'Tecla invalida'
        if i==1:
            a=raw_input('Jugador 1 presione L para lanzar dado: ')
        elif i==2:
            a=raw_input('Jugador 2 presione L para lanzar dado: ')
        elif i==3:
            a=raw_input('Jugador 3 presione L para lanzar dado: ')
        elif i==4:
            a=raw_input('Jugador 4 presione L para lanzar dado: ')
    d=random.randint(1,6)
    print 'El jugador ',i,' obtuvo un ',d,' en el dado ... moviendo ficha.'
    if d!=6:
        return d
    else:
        print 'Puede lanzar una vez mas.'
        return d

#Comer ficha
def comer_ficha(i):
    if i==1:
        if round(j1.xcor())==round(j2.xcor()) and round(j1.ycor())==round(j2.ycor()):
            Jugador2(j2)
        elif round(j1.xcor())==round(j3.xcor()) and round(j1.ycor())==round(j3.ycor()):
            Jugador3(j3)
        elif round(j1.xcor())==round(j4.xcor()) and round(j1.ycor())==round(j4.ycor()):
            Jugador4(j4)
    elif i==2:
        if round(j2.xcor())==round(j1.xcor()) and round(j2.ycor())==round(j1.ycor()):
            Jugador1(j1)
        elif round(j2.xcor())==round(j3.xcor()) and round(j2.ycor())==round(j3.ycor()):
            Jugador3(j3)
        elif round(j2.xcor())==round(j4.xcor()) and round(j2.ycor())==round(j4.ycor()):
            Jugador4(j4)
    elif i==3:
        if round(j3.xcor())==round(j2.xcor()) and round(j3.ycor())==round(j2.ycor()):
            Jugador2(j2)
        elif round(j3.xcor())==round(j1.xcor()) and round(j3.ycor())==round(j1.ycor()):
            Jugador1(j1)
        elif round(j3.xcor())==round(j4.xcor()) and round(j3.ycor())==round(j4.ycor()):
            Jugador4(j4)
    elif i==4:
        if round(j4.xcor())==round(j1.xcor()) and round(j4.ycor())==round(j1.ycor()):
            Jugador1(j1)
        elif round(j4.xcor())==round(j2.xcor()) and round(j4.ycor())==round(j2.ycor()):
            Jugador2(j2)
        elif round(j4.xcor())==round(j3.xcor()) and round(j4.ycor())==round(j3.ycor()):
            Jugador3(j3)
        
#Inicio del Juego
print '				Bienvenido a TurLudo, el ludo de PROGRA USM'
n=int(raw_input('Ingresa cantidad de jugadores [2 a 4 jugadores]: '))
iniciar_juego(n)

#Para dos jugadores
if n==2:
    while j1.pos()!=(0,0) or j2.pos()!=(0,0):
        i=1
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j1.forward(40)
            if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                j1.left(180)
                y=(k-kk)-1
                j1.forward(y*40)
                j1.left(180)
                kk=k
            kk=kk+1

        comer_ficha(i)
                   
        if k==6:
            kk=0
            giro=0
            k=lanzar_dado(i)
            while kk<k:
                j1.forward(40)
                if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                    j1.left(180)
                    y=(k-kk)-1
                    j1.forward(y*40)
                    j1.left(180)
                    kk=k
                kk=kk+1
            
        comer_ficha(i)

        if round(j1.xcor())==(-40) and round(j1.ycor())==(0):
            print 'El jugador 1 gano el juego. ¡FELICITACIONES!'
            break
        
        i=2
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j2.forward(40)
            if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                j2.left(180)
                y=(k-kk)-1
                j2.forward(y*40)
                j2.left(180)
                kk=k
            kk=kk+1

        comer_ficha(i)
       
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j2.forward(40)
                if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                    j2.left(180)
                    y=(k-kk)-1
                    j2.forward(y*40)
                    j2.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)

        if round(j2.xcor())==(40) and round(j2.ycor())==(0):
                print 'El jugador 2 gano el juego. ¡FELICITACIONES!'
                break
            
#Para 3 jugadores
elif n==3:
    while j1.pos()!=(0,0) or j2.pos()!=(0,0) or j3.pos()!=(0,0):
        i=1
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j1.forward(40)
            if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                j1.left(180)
                y=(k-kk)-1
                j1.forward(y*40)
                j1.left(180)
                kk=k
            kk=kk+1
            
        comer_ficha(i)
        
        if k==6:
            kk=0
            giro=0
            k=lanzar_dado(i)
            while kk<k:
                j1.forward(40)
                if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                    j1.left(180)
                    y=(k-kk)-1
                    j1.forward(y*40)
                    j1.left(180)
                    kk=k
                kk=kk+1
            
        comer_ficha(i)
        
        if round(j1.xcor())==(-40) and round(j1.ycor())==(0):
            print 'El jugador 1 gano el juego. ¡FELICITACIONES!'
            break
        
        i=2
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j2.forward(40)
            if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                j2.left(180)
                y=(k-kk)-1
                j2.forward(y*40)
                j2.left(180)
                kk=k
            kk=kk+1
            
        comer_ficha(i)
        
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j2.forward(40)
                if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                    j2.left(180)
                    y=(k-kk)-1
                    j2.forward(y*40)
                    j2.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)
        
        if round(j2.xcor())==(40) and round(j2.ycor())==(0):
                print 'El jugador 2 gano el juego. ¡FELICITACIONES!'
                break
        i=3
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j3.forward(40)
            if round(j3.xcor())==(-280) and round(j3.ycor())==(-40):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(-240):
                j3.left(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(-280):
                j3.left(90)
            elif round(j3.xcor())==(-280) and round(j3.ycor())==(40):
                j3.left(90)
            elif round(j3.xcor())==(280) and round(j3.ycor())==(40):
                j3.left(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(280):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(280):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(-40):
                j3.right(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(-40):
                j3.right(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(40):
                j3.right(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(40):
                j3.right(90)
            elif round(j3.xcor())==(280) and round(j3.ycor())==(-40):
                j3.left(90)
            elif round(j3.xcor())==(0) and round(j3.ycor())==(-240):
                j3.left(90)
            elif round(j3.xcor())==(0) and round(j3.ycor())==(-40):    
                j3.left(180)
                y=(k-kk)-1
                j3.forward(y*40)
                j3.left(180)
                kk=k
            kk=kk+1
            
        comer_ficha(i)
        
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j3.forward(40)
                if round(j3.xcor())==(-280) and round(j3.ycor())==(-40):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(-240):
                    j3.left(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(-280):
                    j3.left(90)
                elif round(j3.xcor())==(-280) and round(j3.ycor())==(40):
                    j3.left(90)
                elif round(j3.xcor())==(280) and round(j3.ycor())==(40):
                    j3.left(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(280):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(280):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(-40):
                    j3.right(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(-40):
                    j3.right(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(40):
                    j3.right(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(40):
                    j3.right(90)
                elif round(j3.xcor())==(280) and round(j3.ycor())==(-40):
                    j3.left(90)
                elif round(j3.xcor())==(0) and round(j3.ycor())==(-240):
                    j3.left(90)
                elif round(j3.xcor())==(0) and round(j3.ycor())==(-40):    
                    j3.left(180)
                    y=(k-kk)-1
                    j3.forward(y*40)
                    j3.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)
        
        if round(j3.xcor())==(0) and round(j3.ycor())==(-40):
                print 'El jugador 3 gano el juego. ¡FELICITACIONES!'
                break
            
#Para 4 jugadores
else:
    n==4
    while j1.pos!=(0,0) or j2.pos!=(0,0) or j3.pos!=(0,0) or j4.pos!=(0,0):
        i=1
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j1.forward(40)
            if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                j1.left(90)
            elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                j1.right(90)
            elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                j1.right(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                j1.left(90)
            elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                j1.left(90)
            elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                j1.left(180)
                y=(k-kk)-1
                j1.forward(y*40)
                j1.left(180)
                kk=k
            kk=kk+1
            
        comer_ficha(i)
        
        if k==6:
            kk=0
            giro=0
            k=lanzar_dado(i)
            while kk<k:
                j1.forward(40)
                if round(j1.xcor())==(-280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-280):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(-40):
                    j1.left(90)
                elif round(j1.xcor())==(280) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(280):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(-40):
                    j1.right(90)
                elif round(j1.xcor())==(40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(40):
                    j1.right(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(40):
                    j1.left(90)
                elif round(j1.xcor())==(-240) and round(j1.ycor())==(0):
                    j1.left(90)
                elif round(j1.xcor())==(-40) and round(j1.ycor())==(0):    
                    j1.left(180)
                    y=(k-kk)-1
                    j1.forward(y*40)
                    j1.left(180)
                    kk=k
                kk=kk+1
            
        comer_ficha(i)
        
        if round(j1.xcor())==(-40) and round(j1.ycor())==(0):
            print 'El jugador 1 gano el juego. ¡FELICITACIONES!'
            break
        
        i=2
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j2.forward(40)
            if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                j2.left(90)
            elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                j2.left(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                j2.right(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                j2.right(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                j2.left(90)
            elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                j2.left(90)
            elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                j2.left(180)
                y=(k-kk)-1
                j2.forward(y*40)
                j2.left(180)
                kk=k
            kk=kk+1

        comer_ficha(i)
        
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j2.forward(40)
                if round(j2.xcor())==(-280) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-280):
                    j2.left(90)
                elif round(j2.xcor())==(-280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(280) and round(j2.ycor())==(40):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(280):
                    j2.left(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(-40):
                    j2.right(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(-40) and round(j2.ycor())==(40):
                    j2.right(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(-40):
                    j2.left(90)
                elif round(j2.xcor())==(240) and round(j2.ycor())==(0):
                    j2.left(90)
                elif round(j2.xcor())==(40) and round(j2.ycor())==(0):    
                    j2.left(180)
                    y=(k-kk)-1
                    j2.forward(y*40)
                    j2.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)
        
        if round(j2.xcor())==(40) and round(j2.ycor())==(0):
                print 'El jugador 2 gano el juego. ¡FELICITACIONES!'
                break
            
        i=3
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j3.forward(40)
            if round(j3.xcor())==(-280) and round(j3.ycor())==(-40):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(-240):
                j3.left(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(-280):
                j3.left(90)
            elif round(j3.xcor())==(-280) and round(j3.ycor())==(40):
                j3.left(90)
            elif round(j3.xcor())==(280) and round(j3.ycor())==(40):
                j3.left(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(280):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(280):
                j3.left(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(-40):
                j3.right(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(-40):
                j3.right(90)
            elif round(j3.xcor())==(40) and round(j3.ycor())==(40):
                j3.right(90)
            elif round(j3.xcor())==(-40) and round(j3.ycor())==(40):
                j3.right(90)
            elif round(j3.xcor())==(280) and round(j3.ycor())==(-40):
                j3.left(90)
            elif round(j3.xcor())==(0) and round(j3.ycor())==(-240):
                j3.left(90)
            elif round(j3.xcor())==(0) and round(j3.ycor())==(-40):    
                j3.left(180)
                y=(k-kk)-1
                j3.forward(y*40)
                j3.left(180)
                kk=k
            kk=kk+1

        comer_ficha(i)
        
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j3.forward(40)
                if round(j3.xcor())==(-280) and round(j3.ycor())==(-40):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(-240):
                    j3.left(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(-280):
                    j3.left(90)
                elif round(j3.xcor())==(-280) and round(j3.ycor())==(40):
                    j3.left(90)
                elif round(j3.xcor())==(280) and round(j3.ycor())==(40):
                    j3.left(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(280):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(280):
                    j3.left(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(-40):
                    j3.right(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(-40):
                    j3.right(90)
                elif round(j3.xcor())==(40) and round(j3.ycor())==(40):
                    j3.right(90)
                elif round(j3.xcor())==(-40) and round(j3.ycor())==(40):
                    j3.right(90)
                elif round(j3.xcor())==(280) and round(j3.ycor())==(-40):
                    j3.left(90)
                elif round(j3.xcor())==(0) and round(j3.ycor())==(-240):
                    j3.left(90)
                elif round(j3.xcor())==(0) and round(j3.ycor())==(-40):    
                    j3.left(180)
                    y=(k-kk)-1
                    j3.forward(y*40)
                    j3.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)
        
        if round(j3.xcor())==(0) and round(j3.ycor())==(-40):
                print 'El jugador 3 gano el juego. ¡FELICITACIONES!'
                break
        i=4
        kk=0
        k=lanzar_dado(i)
        while kk<k:
            j4.forward(40)
            if round(j4.xcor())==(-280) and round(j4.ycor())==(-40):
                j4.left(90)
            elif round(j4.xcor())==(0) and round(j4.ycor())==(240):
                j4.left(90)
            elif round(j4.xcor())==(40) and round(j4.ycor())==(-280):
                j4.left(90)
            elif round(j4.xcor())==(-280) and round(j4.ycor())==(40):
                j4.left(90)
            elif round(j4.xcor())==(280) and round(j4.ycor())==(40):
                j4.left(90)
            elif round(j4.xcor())==(40) and round(j4.ycor())==(240):
                j4.left(90)
            elif round(j4.xcor())==(-40) and round(j4.ycor())==(280):
                j4.left(90)
            elif round(j4.xcor())==(-40) and round(j4.ycor())==(-40):
                j4.right(90)
            elif round(j4.xcor())==(40) and round(j4.ycor())==(-40):
                j4.right(90)
            elif round(j4.xcor())==(40) and round(j4.ycor())==(40):
                j4.right(90)
            elif round(j4.xcor())==(-40) and round(j4.ycor())==(40):
                j4.right(90)
            elif round(j4.xcor())==(280) and round(j4.ycor())==(-40):
                j4.left(90)
            elif round(j4.xcor())==(-40) and round(j4.ycor())==(-280):
                j4.left(90)
            elif round(j4.xcor())==(0) and round(j4.ycor())==(40):    
                j4.left(180)
                y=(k-kk)-1
                j4.forward(y*40)
                j4.left(180)
                kk=k
            kk=kk+1

        comer_ficha(i)
        
        if k==6:
            kk=0
            k=lanzar_dado(i)
            while kk<k:
                j4.forward(40)
                if round(j4.xcor())==(-280) and round(j4.ycor())==(-40):
                    j4.left(90)
                elif round(j4.xcor())==(0) and round(j4.ycor())==(240):
                    j4.left(90)
                elif round(j4.xcor())==(40) and round(j4.ycor())==(-280):
                    j4.left(90)
                elif round(j4.xcor())==(-280) and round(j4.ycor())==(40):
                    j4.left(90)
                elif round(j4.xcor())==(280) and round(j4.ycor())==(40):
                    j4.left(90)
                elif round(j4.xcor())==(40) and round(j4.ycor())==(240):
                    j4.left(90)
                elif round(j4.xcor())==(-40) and round(j4.ycor())==(280):
                    j4.left(90)
                elif round(j4.xcor())==(-40) and round(j4.ycor())==(-40):
                    j4.right(90)
                elif round(j4.xcor())==(40) and round(j4.ycor())==(-40):
                    j4.right(90)
                elif round(j4.xcor())==(40) and round(j4.ycor())==(40):
                    j4.right(90)
                elif round(j4.xcor())==(-40) and round(j4.ycor())==(40):
                    j4.right(90)
                elif round(j4.xcor())==(280) and round(j4.ycor())==(-40):
                    j4.left(90)
                elif round(j4.xcor())==(-40) and round(j4.ycor())==(-280):
                    j4.left(90)
                elif round(j4.xcor())==(0) and round(j4.ycor())==(40):    
                    j4.left(180)
                    y=(k-kk)-1
                    j4.forward(y*40)
                    j4.left(180)
                    kk=k
                kk=kk+1
    
        comer_ficha(i)
        
        if round(j4.xcor())==(0) and round(j4.ycor())==(40):
                print 'El jugador 4 gano el juego. ¡FELICITACIONES!'
                break
#FIN DEL JUEGO
