import random

print("Hallo und herzlich wilkommen beim Tic Tac Toe.")
def Computer():
    gültige_eingabe = False
    while not gültige_eingabe:
        eingabe = input("Mit oder ohne Computer? Gebe 1 für ja ein und 0 für nein!")
        if eingabe == "1" or "0":
            if eingabe == "1":
                gültige_eingabe = True
                return True
            else:
                gültige_eingabe = True
                return False
        else:
            print("Ungültig!")      

#Spielfeld

spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def ausgabe():
    print(" " + spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
    print("__________")
    print(" " + spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
    print("__________")
    print(" " + spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])
    print()

def Zug_Spieler():
    gültige_eingabe = False
    while not gültige_eingabe:
        feld = input("Spieler " + spieler + ", Feld eingeben: ")
        if feld in spielfeld and feld != "x" and feld != "o":
            gültige_eingabe = True
        else:
            print("Ungültig!")   
    return feld 

def Zug_Computer():
    feld = 0
    gültige_eingabe = False
    if spielfeld[0] == spielfeld[1] == "x" and spielfeld[2] != "o":
        feld = 3
    elif spielfeld[1] == spielfeld[2] == "x" and spielfeld[0] != "o":
        feld = 1
    elif spielfeld[3] == spielfeld[4] == "x" and spielfeld[5] != "o":
        feld = 6
    elif spielfeld[4] == spielfeld[5] == "x" and spielfeld[3] != "o":
        feld = 4
    elif spielfeld[6] == spielfeld[7] == "x" and spielfeld[8] != "o":
        feld = 9
    elif spielfeld[7] == spielfeld[8] == "x" and spielfeld[6] != "o":
        feld = 7
    elif spielfeld[0] == spielfeld[3] == "x" and spielfeld[6] != "o":
        feld = 7
    elif spielfeld[3] == spielfeld[6] == "x" and spielfeld[0] != "o":
        feld = 1
    elif spielfeld[1] == spielfeld[4] == "x" and spielfeld[7] != "o":
        feld = 8
    elif spielfeld[4] == spielfeld[7] == "x" and spielfeld[1] != "o":
        feld = 2
    elif spielfeld[2] == spielfeld[5] == "x" and spielfeld[8] != "o": 
        feld = 9                                
    elif spielfeld[5] == spielfeld[8] == "x" and spielfeld[2] != "o":   
        feld = 3
    elif spielfeld[0] == spielfeld[4] == "x" and spielfeld[8] != "o":
        feld = 9
    elif spielfeld[4] == spielfeld[8] == "x" and spielfeld[0] != "o":
        feld = 1
    elif spielfeld[2] == spielfeld[4] == "x" and spielfeld[6] != "o":
        feld = 7
    elif spielfeld[4] == spielfeld[6] == "x" and spielfeld[2] != "o": 
        feld = 3
    elif spielfeld[0] == spielfeld[2] == "x" and spielfeld[1] != "o": 
        feld = 2
    elif spielfeld[3] == spielfeld[5] == "x" and spielfeld[4] != "o": 
        feld = 5
    elif spielfeld[6] == spielfeld[8] == "x" and spielfeld[7] != "o": 
        feld = 8
    elif spielfeld[0] == spielfeld[6] == "x" and spielfeld[3] != "o": 
        feld = 4
    elif spielfeld[1] == spielfeld[7] == "x" and spielfeld[4] != "o": 
        feld = 5
    elif spielfeld[2] == spielfeld[8] == "x" and spielfeld[5] != "o": 
        feld = 6
    elif spielfeld[0] == spielfeld[8] == "x" and spielfeld[4] != "o": 
        feld = 5
    elif spielfeld[2] == spielfeld[6] == "x" and spielfeld[4] != "o": 
        feld = 5                               
    elif spielfeld[0] == "x" and spielfeld[4] != "o":
        feld = 5
    else:
        while not gültige_eingabe:
            feld += 1
            if str(feld) in spielfeld and str(feld) != "x" and str(feld) != "o":
                gültige_eingabe = True
    return feld 

ausgabe()

spieler = "x"
spiel_fertig = False

while not spiel_fertig:   
 
    feld = Zug_Spieler() if spieler == "x" else Zug_Computer()
    spielfeld[int(feld) - 1] = spieler
    
    ausgabe()
    
    if (spielfeld[0] == spielfeld[1] == spielfeld[2]) or \
    (spielfeld[3] == spielfeld[4] == spielfeld[5]) or \
    (spielfeld[6] == spielfeld[7] == spielfeld[8]) or \
    (spielfeld[0] == spielfeld[3] == spielfeld[6]) or \
    (spielfeld[1] == spielfeld[4] == spielfeld[7]) or \
    (spielfeld[2] == spielfeld[5] == spielfeld[8]) or \
    (spielfeld[0] == spielfeld[4] == spielfeld[8]) or \
    (spielfeld[2] == spielfeld[4] == spielfeld[6]):
        print("Glückwunsch Spieler " + spieler + ", du hast gewonnen")
        spiel_fertig = True
    
    spieler = "o" if spieler == "x" else "x"