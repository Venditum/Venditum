from turtle import *

nummer = 0
x = 0
liste = []

Zahl = 1
vorherigezahl = 0
Nummer = 0
vorherigezahl2 = 0

while Nummer <= 1000:
    liste.append(Zahl)
    vorherigezahl2 = vorherigezahl
    vorherigezahl = Zahl
    Zahl = vorherigezahl + vorherigezahl2
    Nummer += 1

def flocke(stufe, länge):
    if stufe == 0:
        forward(länge)
    else:
        flocke(stufe - 1, länge / 3)
        left(60)
        flocke(stufe - 1, länge / 3)  
        right(120)
        flocke(stufe - 1, länge / 3) 
        left(60)
        flocke(stufe - 1, länge / 3)    
        
speed(0)
penup()
left(90)
forward(300)
right(90)
backward(200)
pendown()
while nummer < 360:
    for x in range(90):
        forward(liste[nummer] / 5)
        right(1)    
    nummer += 1   

done()    