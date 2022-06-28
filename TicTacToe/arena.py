from spielfeld import Spielfeld
from mensch import Spieler

class Arena:
    def __init__(self):
        pass

    def spielen(self, spieler1, spieler2):
        Spielfeld_neu = Spielfeld([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        Spielfeld_neu.ausgabe()
        while not Spielfeld_neu.vorbei:
            spieler1.zug()
            spieler2.zug()

     