class spieler_mensch:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def zug(self, spielfeld):
        gültige_eingabe = False
        while not gültige_eingabe:
            feld = input(self.name + ", bitte ein Feld eingeben:")
            if feld in spielfeld and feld != "x" and feld != "o":
                gültige_eingabe = True
            else:
                print("Ungültig")
        return feld