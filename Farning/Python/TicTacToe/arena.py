from spieler_mensch import spieler_mensch
from KI import Level_1
from KI import Level_2
from KI import TTT_God
import random

class Arena:
    def __init__(self, spielfeld):
        self.spielfeld = spielfeld

    def __ausgabe(self):
        print("")
        print(" " + self.spielfeld[0] + " | " + self.spielfeld[1] + " | " + self.spielfeld[2])
        print("___________")
        print(" " + self.spielfeld[3] + " | " + self.spielfeld[4] + " | " + self.spielfeld[5])
        print("___________")
        print(" " + self.spielfeld[6] + " | " + self.spielfeld[7] + " | " + self.spielfeld[8])
        print("")

    def __gewinnprüfung(self):
        return self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2] or \
                self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5] or \
                self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6] or \
                self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7] or \
                self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8] or \
                self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]

    def gewinnüberprüfung(self):
        for i in range(9):
            if self.spielfeld[i - 1] == str(i):
                return False
        return True        

    def spielen(self ,spieler1, spieler2):
        self.spielfeld = ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"] 
        
        spieler = random.choice([spieler1, spieler2])

        if spieler == spieler:
            spieler1.symbol = "x"
            spieler2.symbol = "o"
        else:
            spieler1.symbol = "o"
            spieler2.symbol = "x"

        spiel_fertig = False

        spieler = spieler1.symbol

        while not spiel_fertig:
            
            feld = spieler1.zug(self.spielfeld) if spieler == spieler1.symbol else spieler2.zug(self.spielfeld)
            
            self.spielfeld[int(feld) - 1 ] = spieler

            #self.__ausgabe()

            if self.__gewinnprüfung():
                spiel_fertig = True
                gewinner = spieler

            if self.gewinnüberprüfung():
                spiel_fertig = True
                gewinner = "unentschieden"    

            spieler = spieler2.symbol if spieler == spieler1.symbol else spieler1.symbol

        return gewinner    
            
a = Arena(["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"])
s1 = spieler_mensch("Johannes", " ")
s2 = spieler_mensch("Hirakula", " ")
s3 = Level_1("Computer1")
s4 = Level_2("Computer2")
s5 = Level_2("Computer3")
s6 = TTT_God("Unbesiegbar", " ", " ")
s7 = TTT_God("Unbesiegbar2", " ", " ")

wins1 = 0
wins2 = 0

for i in range(1000):
    x = a.spielen(s4, s5)
    if x == s4.symbol:
        wins1 += 1
    if x == s5.symbol:
        wins2 += 1
    print(i)

print(wins1, wins2)