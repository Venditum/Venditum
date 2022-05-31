from mailbox import Babyl


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
    
    class Tier_Baby:
        def __init__(self, tierart: str, nahrung: list, fressfeinde: list, gewicht: float, größe: int, farbe: str):
            self.tierart = tier1.tierart
            self.nahrung = tier1.nahrung
            self.fressfeinde = tier1.fressfeinde
            self.gewicht = tier1.gewicht / 5      
            self.größe = tier1.größe / 5
            self.farbe = tier1.farbe
                
tier1 = Tier("Löwe", ["Zebra", "Gazelle", "Gnu"], [], 150.0, 150, "gelb")
tier2 = Tier("Zebra", ["Gras"], ["Löwe"], 300.0, 210, "schwarz-weiß")
tier3 = Tier("Gnu", ["Gras"], ["Löwe"], 200.0, 190, "schwarz")

babytier1 = Tier.Tier_Baby(tier1, tier1, tier1, tier1, tier1, tier1)
print(babytier1.gewicht)

