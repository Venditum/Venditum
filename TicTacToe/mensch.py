from spielfeld import Spielfeld

class Spieler:
    def __init__(self):
        pass
    def zug(self, spielfeld):
        gültige_eingabe = False
        while not gültige_eingabe:
            feld = input("Bitte Feld eingeben!")
            if feld in spielfeld:
                gültige_eingabe = True
            else:
                print("Ungültig!")    
        spielfeld.feldverkleinerung(feld)
        spielfeld.besetzung(feld)              
        return spielfeld 