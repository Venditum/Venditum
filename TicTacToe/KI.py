import random

class Level_1:
    def __init__(self, name):
        self.name = name

    def zug(self, spielfeld):
        gültige_eingabe = False
        while not gültige_eingabe:
            x = random.choice(spielfeld)
            if x in spielfeld and x != "x" and x!= "o":
                gültige_eingabe = True
        return x  

class Level_2:
    def __init__(self, name):
        self.name = name
    
    def zug(self, spielfeld):
        feld = 0
        gültige_eingabe = False
        if spielfeld[0] == spielfeld[1] == "x" and spielfeld[2] != "o":
            feld = 3
        elif spielfeld[1] == spielfeld[2] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[3] == spielfeld[4] == "x" and spielfeld[5] != "o":
            feld = 6
        elif spielfeld[4] == spielfeld[5] == "x" and spielfeld[3] != "o":
            feld = 4
        elif spielfeld[6] == spielfeld[7] == "x" and spielfeld[8] != "o":
            feld = 9
        elif spielfeld[7] == spielfeld[8] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[0] == spielfeld[3] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[3] == spielfeld[6] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[1] == spielfeld[4] == "x" and spielfeld[7] != "o":
            feld = 8
        elif spielfeld[4] == spielfeld[7] == "x" and spielfeld[1] != "o":
            feld = 2
        elif spielfeld[2] == spielfeld[5] == "x" and spielfeld[8] != "o": 
            feld = 9                                
        elif spielfeld[5] == spielfeld[8] == "x" and spielfeld[2] != "o":   
            feld = 3
        elif spielfeld[0] == spielfeld[4] == "x" and spielfeld[8] != "o":
            feld = 9
        elif spielfeld[4] == spielfeld[8] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[2] == spielfeld[4] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[4] == spielfeld[6] == "x" and spielfeld[2] != "o": 
            feld = 3
        elif spielfeld[0] == spielfeld[2] == "x" and spielfeld[1] != "o": 
            feld = 2
        elif spielfeld[3] == spielfeld[5] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[6] == spielfeld[8] == "x" and spielfeld[7] != "o": 
            feld = 8
        elif spielfeld[0] == spielfeld[6] == "x" and spielfeld[3] != "o": 
            feld = 4
        elif spielfeld[1] == spielfeld[7] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[2] == spielfeld[8] == "x" and spielfeld[5] != "o": 
            feld = 6
        elif spielfeld[0] == spielfeld[8] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[2] == spielfeld[6] == "x" and spielfeld[4] != "o": 
            feld = 5                               
        elif spielfeld[0] == spielfeld[1] == "o" and spielfeld[2] != "x":
            feld = 3
        elif spielfeld[1] == spielfeld[2] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[3] == spielfeld[4] == "o" and spielfeld[5] != "x":
            feld = 6
        elif spielfeld[4] == spielfeld[5] == "o" and spielfeld[3] != "x":
            feld = 4
        elif spielfeld[6] == spielfeld[7] == "o" and spielfeld[8] != "x":
            feld = 9
        elif spielfeld[7] == spielfeld[8] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[0] == spielfeld[3] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[3] == spielfeld[6] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[1] == spielfeld[4] == "o" and spielfeld[7] != "x":
            feld = 8
        elif spielfeld[4] == spielfeld[7] == "o" and spielfeld[1] != "x":
            feld = 2
        elif spielfeld[2] == spielfeld[5] == "o" and spielfeld[8] != "x": 
            feld = 9                                
        elif spielfeld[5] == spielfeld[8] == "o" and spielfeld[2] != "x":   
            feld = 3
        elif spielfeld[0] == spielfeld[4] == "o" and spielfeld[8] != "x":
            feld = 9
        elif spielfeld[4] == spielfeld[8] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[2] == spielfeld[4] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[4] == spielfeld[6] == "o" and spielfeld[2] != "x": 
            feld = 3
        elif spielfeld[0] == spielfeld[2] == "o" and spielfeld[1] != "x": 
            feld = 2
        elif spielfeld[3] == spielfeld[5] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[6] == spielfeld[8] == "o" and spielfeld[7] != "x": 
            feld = 8
        elif spielfeld[0] == spielfeld[6] == "o" and spielfeld[3] != "x": 
            feld = 4
        elif spielfeld[1] == spielfeld[7] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[2] == spielfeld[8] == "o" and spielfeld[5] != "x": 
            feld = 6
        elif spielfeld[0] == spielfeld[8] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[2] == spielfeld[6] == "o" and spielfeld[4] != "x": 
            feld = 5                               
        elif spielfeld[0] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[2] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[6] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[8] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[4] == "x" and spielfeld[0] != "o":  
            feld = 1
        elif spielfeld[1] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[3] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[5] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[7] == "x" and spielfeld[4] != "o":  
            feld = 5       

        else:
            while not gültige_eingabe:
                feld += 1
                if str(feld) in spielfeld and str(feld) != "x" and str(feld) != "o":
                    gültige_eingabe = True
        return feld        

class TTT_God:
    def __init__(self, name, symbol, symbol_gegner):
        self.name = name
        self.symbol = symbol
        self.symbol_gegner = symbol_gegner
    
    def gewinnprüfung(self, spielfeld):
        return spielfeld[0] == spielfeld[1] == spielfeld[2] or \
                spielfeld[3] == spielfeld[4] == spielfeld[5] or \
                spielfeld[6] == spielfeld[7] == spielfeld[8] or \
                spielfeld[0] == spielfeld[3] == spielfeld[6] or \
                spielfeld[1] == spielfeld[4] == spielfeld[7] or \
                spielfeld[2] == spielfeld[5] == spielfeld[8] or \
                spielfeld[0] == spielfeld[4] == spielfeld[8] or \
                spielfeld[2] == spielfeld[4] == spielfeld[6]
    
    def freie_felder(self, spielfeld):
        return [freies_feld for freies_feld in spielfeld if freies_feld not in ["x", "o"]]
    
    def bewertung(self, spielfeld: list, symbol: str):
        if symbol == self.symbol:
            if self.gewinnprüfung(spielfeld):
                return -(len(self.freie_felder(spielfeld)) + 1)
            if len(self.freie_felder(spielfeld)) == 0:
                return 0    
            max = -10
            bewertung = 0
            for freies_feld in self.freie_felder(spielfeld):
                spielfeld[int(freies_feld) - 1] = self.symbol
                bewertung = self.bewertung(spielfeld, self.symbol_gegner)
                spielfeld[int(freies_feld) - 1] = freies_feld 
                if bewertung > max:
                    max = bewertung
            return max
        else: 
            if self.gewinnprüfung(spielfeld):
                return len(self.freie_felder(spielfeld)) + 1
            if len(self.freie_felder(spielfeld)) == 0:
                return 0    
            min = 10
            bewertung = 0
            for freies_feld in self.freie_felder(spielfeld):
                spielfeld[int(freies_feld) - 1] = self.symbol_gegner
                bewertung = self.bewertung(spielfeld, self.symbol)
                spielfeld[int(freies_feld) - 1] = freies_feld                 
                if bewertung < min:
                    min = bewertung  
            return min
    
    def minimax(self, spielfeld):
        max = -10
        bestes_feld = 0
        for freies_feld in self.freie_felder(spielfeld):
            spielfeld[int(freies_feld) - 1] = self.symbol
            bewertung = self.bewertung(spielfeld, self.symbol_gegner)
            if bewertung > max:
                max = bewertung
                bestes_feld = freies_feld
            spielfeld[int(freies_feld) - 1] = freies_feld
            #print(bestes_feld)
        return bestes_feld

    def zug(self, spielfeld):
        self.symbol_gegner = "x" if self.symbol == "o" else "o"
        return int(self.minimax(spielfeld)) - 1   
