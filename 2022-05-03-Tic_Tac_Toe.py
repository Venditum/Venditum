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
    print("__________")

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
    gültige_eingabe = False
    while not gültige_eingabe:
        x = random.choice(spielfeld)
        if type(int(x)) == int:
            feld = x
        if feld in spielfeld and feld != "x" and feld != "o":
            gültige_eingabe = True  
    return feld 

ausgabe()

def Zug_Computer_Verbessert():
    Zeile_1 = [0, 1, 2]
    Zeile_2 = [3, 4, 5]
    Zeile_3 = [0, 1, 2]
    Spalte_1 = [0, 1, 2]
    Spalte_2 = [0, 1, 2]
    Spalte_3 = [0, 1, 2]
    Diagonale_1 = [0, 1, 2]
    Diagonale_2 = [0, 1, 2]

spieler = "x"
spiel_fertig = False

while not spiel_fertig:   
 
    feld = Zug_Spieler() if spieler == "x" else Zug_Computer()
     
    spielfeld[int(feld) - 1] = spieler
    
    ausgabe()
    
    if (spielfeld[0] == spielfeld[1] and spielfeld[2] == spieler) or \
    (spielfeld[3] == spielfeld[4] == spielfeld[5] == spieler) or \
    (spielfeld[6] == spielfeld[7] == spielfeld[8] == spieler) or \
    (spielfeld[0] == spielfeld[3] == spielfeld[6] == spieler) or \
    (spielfeld[1] == spielfeld[4] == spielfeld[7] == spieler) or \
    (spielfeld[2] == spielfeld[5] == spielfeld[8] == spieler) or \
    (spielfeld[0] == spielfeld[4] == spielfeld[8] == spieler) or \
    (spielfeld[2] == spielfeld[4] == spielfeld[6] == spieler):
        print("Glückwunsch Spieler " + spieler + ", du hast gewonnen")
        spiel_fertig = True
    
    spieler = "o" if spieler == "x" else "x"