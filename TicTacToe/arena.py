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


    def spielen(self ,spieler1, spieler2):
        spieler1.symbol = "x"
        spieler2.symbol = "o"
        spieler = "o"

        spiel_fertig = False

        while not spiel_fertig:
            
            feld = spieler1.zug(self.spielfeld) if spieler == spieler1 else spieler2.zug(self.spielfeld)
            
            self.spielfeld[int(feld) - 1 ] = spieler

            self.__ausgabe()

            if self.__gewinnprüfung():
                spiel_fertig = True
                gewinner = spieler

            spieler = spieler2.symbol if spieler == spieler1.symbol else spieler1.symbol

        return gewinner    
            
a = Arena(["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"])
s1 = spieler_mensch("Johannes")
s2 = spieler_mensch("Hirakula")
s3 = Level_1("Computer1")
s4 = Level_2("Computer2")
s5 = TTT_God("Unbesiegbar", "o", "x")
for i in range(1000):
    wins1 = 0
    wins2 = 0
    x = a.spielen(s3, s5)
    if x == "Computer1":
        wins1 += 1
    if x == "Computer2":
        wins2 += 1

print(wins1, wins2)
