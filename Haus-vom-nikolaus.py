from turtle import *

nummer = 0
x = 0

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
    x += 0.01
    flocke(2 , 12)
    right(x)    
    nummer += 1   

done()    