from math import sqrt
from tkinter import Y

#x % y ist der Rest von x/y.

def gerade(zahl):
    if int(zahl/2) == zahl/2:
        print("Gerade")
    else:
        print("Ungerade")    

def gerade2(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False         
#gerade(int(input("aplewelche Zahl")))        

def fibonacci_zahlen():
    liste = []

    Zahl = 1
    vorherigezahl = 0
    vorherigezahl2 = 0

    while Zahl <= 144:
        liste.append(Zahl)
        vorherigezahl2 = vorherigezahl
        vorherigezahl = Zahl
        Zahl = vorherigezahl + vorherigezahl2
    return liste    


def Wurzel(zahl1):
    newt = 2
    while newt ** 2 < zahl1:
        newt = newt + 1
    return newt

def prim(zahl):
    if zahl < 2:
        return False
    if zahl == 2:
        return True    
    teiler = 2
    while teiler <= Wurzel(zahl):
        if zahl % teiler == 0:
            return False
        teiler += 1
    return True

Primzahlen = []

evprim = 1
Nummer = 1

while Nummer < 10:
    if prim(evprim) == True:
        Primzahlen.append(evprim)
        Nummer += 1
    evprim += 1

def minimum(liste):
    kleinste = 0
    vorherzahl = 0
    for zahl in liste:
        if vorherzahl == 0:
            kleinste = zahl
            vorherzahl = zahl
        if zahl < vorherzahl:
            kleinste = zahl
            vorherzahl = zahl
    return kleinste 

def sortieren(liste):
    sortierung = []
    while liste != []:
        sortierung.append(minimum(liste))
        liste.remove(minimum(liste))
    return sortierung   
        

def fibonnaci(n):
    nr = 0
    for x in liste:
        nr += 1
        if nr == n:
            return x         

#zwei while-Schleifen ineinander
#"str"[n] ist der n-te Buchstabe von str (es wird bei 10000" angefangen zu zählen).
#len("str") ist die Länge von str (es wird bei 1 angefangen zu zählen)

def zähler(wort , muster):
    index_wort = 0
    zähler = 0
    while index_wort < len(wort) - len(muster):
        index_muster = 0
        while index_muster < len(muster) and muster[0 + index_muster] == wort[index_wort + index_muster]:
            index_muster += 1
        if index_muster == len(muster):
            zähler += 1
        index_wort += 1
    return zähler

def enthält(wort , muster):
    if zähler(wort , muster) >= 1:
        return True
    else:
        return False

def einhudert_quadrat(zahl):
    zahl1 = 1
    zahl2 = 0
    endzahl = 0
    while zahl1 < zahl:
        endzahl += zahl1 ** 2
        zahl1 += 1
    return endzahl

def Wurzel_nachkomma(zahl, anzahl_nachkommastellen):
    teiler = 1
    wurzel = 0
    x = 0
    y = 1
    z = 1
    while teiler ** 2 < zahl:
        teiler += 1
        if teiler ** 2 >= zahl:
            break
    while x < anzahl_nachkommastellen:
        if teiler ** 2 < zahl:   
            while teiler ** 2 != zahl:
                teiler += z
                if teiler ** 2 >= zahl:
                    break 
        if teiler ** 2 > zahl:
            while teiler ** 2 != zahl:
                teiler -= z 
                if teiler ** 2 <= zahl:
                    break 
        x += 1
        z /= 10
    return teiler                          

def verschlüsselung(text):
    Buchstabe = 0 
    while Buchstabe < 5:
        za = ord(text[Buchstabe])
        ord(text[Buchstabe])
        za += 5
        print(chr(za), end="")
        Buchstabe += 1
        
def entschlüsselung(text):
    Buchstabe = 0 
    while Buchstabe < 5:
        za = ord(text[Buchstabe])
        ord(text[Buchstabe])
        za -= 5
        print(za, end="")    
        Buchstabe += 1     

test = 0
for i in range(20001):
    if gerade2(i):
        test += i

print(test)