import random

class Tier:
    def __init__(self, tierart: str, nahrung: list, fressfeinde: list, gewicht: float, größe: int, farbe: str):
        self.tierart = tierart
        self.nahrung = nahrung
        self.fressfeinde = fressfeinde
        self.gewicht = gewicht
        self.größe = größe
        self.farbe = farbe    

    def __str__(self) -> str:
            return "Tierart: " + str(self.tierart) + " Gewicht: " + str(self.gewicht) + " Größe: " + str(self.größe) + " Farbe: " + str(self.farbe)

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
    
    def junges(self) -> "Tier":
        junges_tierart = self.tierart
        junges_nahrung = self.nahrung
        junges_fressfeinde = self.fressfeinde
        junges_gewicht = round(random.uniform(self.gewicht * 0.15, self.gewicht * 0.05), 2)      
        junges_größe = int(random.uniform(self.größe * 0.15, self.größe * 0.05))
        junges_farbe = self.farbe
        junges = Tier(junges_tierart, junges_nahrung, junges_fressfeinde, junges_gewicht, junges_größe, junges_farbe)
        return junges

class Safaripark:
    def __init__(self,name: str, tiere: list, tourpreis: float):
        self.name = name
        self.tiere = tiere
        self.tourpreis = tourpreis
    def Besucher(self):
        Alter = input("Wie alt sind sie")
        if Alter < 1:
            self.tourpreis = 0
        if Alter > 1 and Alter < 17:
            self.tourpreis -= 2
        if Alter > 18 and Alter < 65:
            self.tourpreis += 1
        if Alter > 65:
            self.tourpreis -= 1          
        return self.tourpreis    
    def anzahl_tiere(self) -> int:
        return len(self.tiere) 
    def preis_pro_tier(self) -> float:
        return self.tourpreis / len(self.tiere)
    def aufnehmen(self, tier: Tier) -> None:
        self.tiere.append(tier)
        return self.tiere
    def anzahl_tierart(self, tierart) -> int:
        anzahl_tierart = 0
        for x in self.tiere:
            if x == tierart:
                anzahl_tierart += 1
        return anzahl_tierart        
    def gesamtgewicht(self) -> float:
        gesamtgewicht = 0
        for x in self.tiere:
            gesamtgewicht += x.gewicht
        return gesamtgewicht
    def Safaripark_ist_leer(self) -> bool:
        return len(self.tiere) == 0  
    def schwerstes(self) -> Tier:
        if self.Safaripark_ist_leer:
            raise ValueError("Der Zoo ist ller!")
        schwerstes = ""
        bisherschwerstes_gewicht = 0
        bisherschwerstes = ""
        for x in self.tiere:
            if x.gewicht > bisherschwerstes_gewicht:
                bisherschwerstes_gewicht = x.gewicht
                bisherschwerstes = x
        schwerstes = bisherschwerstes
        return schwerstes
    def geburt(self) -> Tier:
        junges = random.choice(self.tiere).junges()
        self.aufnehmen(junges)
        return junges
    def tierezählen(self) -> dict:
        arten = {}
        for tier in self.tiere:
            if tier.tierart not in arten:
                arten.update({tier.tierart: 1})
            else:
                arten[tier.tierart] += 1
        return arten
    def tierarten(self):
        arten = []
        for tier in self.tiere:
            if tier.tierart not in arten:
                arten.append(tier.tierart)
        return arten    
    def häufigste_tierart(self) -> str:
        übergang = self.tierezählen()
        häufigstes = 0 
        for key, value in übergang.items():
            if value > häufigstes:
                häufigstes = value
                tier = key
        return tier
    def häufigste_tierart_2(self) -> str:
        häufigste_anzahl = 0
        häufigstes_tier = ""
        liste = self.tierarten()
        for tier in liste:
            anzahl = self.anzahl_tierart(tier)
            if anzahl > häufigste_anzahl:
                häufigste_anzahl = anzahl
                häufigstes_tier = tier
            print(tier)
        print(häufigstes_tier)
        return häufigstes_tier        

tier1 = Tier("Löwe", ["Zebra", "Gazelle", "Gnu"], [], 150.0, 150, "gelb")
tier2 = Tier("Zebra", ["Gras"], ["Löwe"], 300.0, 210, "schwarz-weiß")
tier3 = Tier("Gnu", ["Gras"], ["Löwe"], 200.0, 190, "schwarz")
Safaripark_Venditum = Safaripark("Venditum", [tier1, tier2, tier2, tier3, tier1, tier1, tier3], 10)
print(Safaripark_Venditum.anzahl_tierart(tier1))