class Tier:
    def __init__(self, tierart: str, nahrung: list, fressfeinde: list, gewicht: float, größe: int, farbe: str):
        self.tierart = tierart
        self.nahrung = nahrung
        self.fressfeinde = fressfeinde
        self.gewicht = gewicht
        self.größe = größe
        self.farbe = farbe    

    def __str__(self) -> str:
            return "Tierart: " + str(self.tierart) + "Gewicht: " + str(self.gewicht) + "Größe: " + str(self.farbe) + "Farbe: " + str(self.farbe)

    def fressen(self) -> float:
        self.gewicht *= 1.1
        return self.gewicht

    def füttern(self, futtergewicht: float) -> float:
        self.gewicht += futtergewicht * 0.5
        return self.gewicht

    def wachsen(self, tage: int) -> None:
        self.gewicht *= 1.01 ** tage
        self.größe *= 1.005 ** tage 
        return self.gewicht, self.größe

tier1 = Tier("Löwe", ["Zebra", "Gazelle", "Gnu"], [], 150.0, 150, "gelb")
tier2 = Tier("Zebra", ["Gras"], ["Löwe"], 300.0, 210, "schwarz-weiß")
tier3 = Tier("Gnu", ["Gras"], ["Löwe"], 200.0, 190, "schwarz")

print(tier3.wachsen(30))
