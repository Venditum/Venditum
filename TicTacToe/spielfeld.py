class Spielfeld:
    def __init__(self, felder: list, felder_übrig: list):
        self.felder = felder
        self.felder_übrig = felder_übrig

    def ausgabe(self):
        print(" " + self.felder[0] + " | " + self.felder[1] + " | " + self.felder[2])
        print("__________")
        print(" " + self.felder[3] + " | " + self.felder[4] + " | " + self.felder[5])
        print("__________")
        print(" " + self.felder[6] + " | " + self.felder[7] + " | " + self.felder[8])
        print()

    def besetzung(self, feld, spieler):
        self.felder[feld - 1] = spieler
    
    def feldverkleinerung(self, feld):
        self.felder.remove(feld)

    def vorbei(self):
        if (self.felder[0] == self.felder[1] == self.felder[2]) or \
        (self.felder[3] == self.felder[4] == self.felder[5]) or \
        (self.felder[6] == self.felder[7] == self.felder[8]) or \
        (self.felder[0] == self.felder[3] == self.felder[6]) or \
        (self.felder[1] == self.felder[4] == self.felder[7]) or \
        (self.felder[2] == self.felder[5] == self.felder[8]) or \
        (self.felder[0] == self.felder[4] == self.felder[8]) or \
        (self.felder[2] == self.felder[4] == self.felder[6]):
            return True
        else:
            return False            

