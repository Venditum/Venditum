def verschlüsselung(text):
    Buchstabe = 0
    ergebnis = ""
    while Buchstabe < len(text): 
        za = text[Buchstabe]
        if za == "a":
            za = "000110"  
        if za == "b":
            za = "00111"
        if za == "c":
            za = "001000" 
        if za == "d":
            za = "001001"  
        if za == "e":
            za = "001010"
        if za == "f":
            za = "001011"     
        if za == "g":
            za = "001100"  
        if za == "h":
            za = "001101"
        if za == "i":
            za = "001110"  
        if za == "j":
            za = "001111"  
        if za == "k":
            za = "010000"
        if za == "l":
            za = "010001" 
        if za == "m":
            za = "010010"  
        if za == "n":
            za = "010011"
        if za == "o":
            za = "010100"     
        if za == "p":
            za = "010101"  
        if za == "q":
            za = "010110"
        if za == "r":
            za = "010111"
        if za == "s":
            za = "011000"  
        if za == "t":
            za = "011001"
        if za == "u":
            za = "011010" 
        if za == "v":
            za = "000001"  
        if za == "w":
            za = "000010"
        if za == "x":
            za = "000011"     
        if za == "y":
            za = "000100"  
        if za == "z":
            za = "000101"
        if za == "A":
            za = "100110"  
        if za == "B":
            za = "100111"
        if za == "C":
            za = "101000" 
        if za == "D":
            za = "101001"  
        if za == "E":
            za = "101010"
        if za == "F":
            za = "101011"     
        if za == "G":
            za = "101100"  
        if za == "H":
            za = "101101"
        if za == "I":
            za = "101110"  
        if za == "J":
            za = "101111"  
        if za == "K":
            za = "110000"
        if za == "L":
            za = "110001" 
        if za == "M":
            za = "110010"  
        if za == "N":
            za = "110011"
        if za == "O":
            za = "110100"     
        if za == "P":
            za = "110101"  
        if za == "Q":
            za = "110110"
        if za == "R":
            za = "110111"
        if za == "S":
            za = "111000"  
        if za == "T":
            za = "111001"
        if za == "U":
            za = "111010" 
        if za == "V":
            za = "100001"  
        if za == "W":
            za = "100010"
        if za == "X":
            za = "100011"     
        if za == "Y":
            za = "100100"  
        if za == "Z":
            za = "100101"    
        if za == ".":
            za = "011011"
        if za == ",":
            za = "011100"
        if za == "?":
            za = "011101"
        if za == "!":
            za = "011110"
        if za == ":":
            za = "011111"   
        if za == " ":
            za = "000000"         
        ergebnis += za
        Buchstabe += 1
    return ergebnis

def entschlüsselung(text):
    Buchstabe = 0
    Zwischenablage = ""
    ergebnis = ""
    while Buchstabe <= len(text): 
        x = Buchstabe + 6
        za = Buchstabe
        if x <= len(text):
            while Buchstabe <= za + 5:
                Zwischenablage += text[Buchstabe]
                Buchstabe += 1
        Buchstabe = za
        if Zwischenablage == "000001":
            Zwischenablage = "v"  
        if Zwischenablage == "000010":
            Zwischenablage = "w"
        if Zwischenablage == "000011":
            Zwischenablage = "x" 
        if Zwischenablage == "000100":
            Zwischenablage = "y"  
        if Zwischenablage == "000101":
            Zwischenablage = "z"
        if Zwischenablage == "000110":
            Zwischenablage = "a"     
        if Zwischenablage == "000111":
            Zwischenablage = "b"  
        if Zwischenablage == "001000":
            Zwischenablage = "c"
        if Zwischenablage == "001001":
            Zwischenablage = "d"  
        if Zwischenablage == "001010":
            Zwischenablage = "e"  
        if Zwischenablage == "001011":
            Zwischenablage = "f"
        if Zwischenablage == "001100":
            Zwischenablage = "g" 
        if Zwischenablage == "001101":
            Zwischenablage = "h"  
        if Zwischenablage == "001110":
            Zwischenablage = "i"
        if Zwischenablage == "001111":
            Zwischenablage = "j"     
        if Zwischenablage == "010000":
            Zwischenablage = "k"  
        if Zwischenablage == "010001":
            Zwischenablage = "l"
        if Zwischenablage == "010010":
            Zwischenablage = "m"
        if Zwischenablage == "010011":
            Zwischenablage = "n"  
        if Zwischenablage == "010100":
            Zwischenablage = "o"
        if Zwischenablage == "010101":
            Zwischenablage = "p" 
        if Zwischenablage == "010110":
            Zwischenablage = "q"  
        if Zwischenablage == "010111":
            Zwischenablage = "r"
        if Zwischenablage == "011000":
            Zwischenablage = "s"     
        if Zwischenablage == "011001":
            Zwischenablage = "t"  
        if Zwischenablage == "011010":
            Zwischenablage = "u"
        if Zwischenablage == "100001":
            Zwischenablage = "V"  
        if Zwischenablage == "100010":
            Zwischenablage = "W"
        if Zwischenablage == "100011":
            Zwischenablage = "X" 
        if Zwischenablage == "100100":
            Zwischenablage = "Y"  
        if Zwischenablage == "100101":
            Zwischenablage = "Z"
        if Zwischenablage == "100110":
            Zwischenablage = "A"     
        if Zwischenablage == "100111":
            Zwischenablage = "B"  
        if Zwischenablage == "101000":
            Zwischenablage = "C"
        if Zwischenablage == "101001":
            Zwischenablage = "D"  
        if Zwischenablage == "101010":
            Zwischenablage = "E"  
        if Zwischenablage == "101011":
            Zwischenablage = "F"
        if Zwischenablage == "101100":
            Zwischenablage = "G" 
        if Zwischenablage == "101101":
            Zwischenablage = "H"  
        if Zwischenablage == "101110":
            Zwischenablage = "I"
        if Zwischenablage == "101111":
            Zwischenablage = "J"     
        if Zwischenablage == "110000":
            Zwischenablage = "K"  
        if Zwischenablage == "110001":
            Zwischenablage = "L"
        if Zwischenablage == "110010":
            Zwischenablage = "M"
        if Zwischenablage == "110011":
            Zwischenablage = "N"  
        if Zwischenablage == "110100":
            Zwischenablage = "O"
        if Zwischenablage == "110101":
            Zwischenablage = "P" 
        if Zwischenablage == "110110":
            Zwischenablage = "Q"  
        if Zwischenablage == "110111":
            Zwischenablage = "R"
        if Zwischenablage == "111000":
            Zwischenablage = "S"     
        if Zwischenablage == "111001":
            Zwischenablage = "T"  
        if Zwischenablage == "111010":
            Zwischenablage = "U"  
        if Zwischenablage == "011011":
              Zwischenablage = "."
        if Zwischenablage == "011100":
            Zwischenablage = ","
        if Zwischenablage == "011101":
            Zwischenablage = "?"
        if Zwischenablage == "011110":
            Zwischenablage = "!"
        if Zwischenablage == "011111":
            Zwischenablage = ":"   
        if Zwischenablage == "000000":
            Zwischenablage = " "           
        ergebnis += Zwischenablage
        Buchstabe += 6 
        Zwischenablage = ""
    return ergebnis 

def verschlüsselung_involutorisch(text: str) -> str:
    text_versclüsselt = ""
    for Zeichen in text:
        ascii_position = ord(Zeichen)
        alphabet_position = ascii_position - ord("a")
        alphabet_position_neu = (alphabet_position + 13) % 26
        ascii_position_neu = alphabet_position_neu + ord("a")
        zeichen_neu = chr(ascii_position_neu)
        text_versclüsselt += zeichen_neu
    return text_versclüsselt 

def verschlüsselung_verschiebung(text: str, Verschiebung: int) -> str:
    text_versclüsselt = ""
    for Zeichen in text:
        ascii_position = ord(Zeichen)
        alphabet_position = ascii_position - ord("a")
        alphabet_position_neu = (alphabet_position + Verschiebung) % 26
        ascii_position_neu = alphabet_position_neu + ord("a")
        zeichen_neu = chr(ascii_position_neu)
        text_versclüsselt += zeichen_neu
    return text_versclüsselt 

def entschlüsselung_verschiebung(text: str, Verschiebung: int) -> str:
    text_versclüsselt = ""
    for Zeichen in text:
        ascii_position = ord(Zeichen)
        alphabet_position = ascii_position - ord("a")
        alphabet_position_neu = (alphabet_position - Verschiebung) % 26
        ascii_position_neu = alphabet_position_neu + ord("a")
        zeichen_neu = chr(ascii_position_neu)
        text_versclüsselt += zeichen_neu
    return text_versclüsselt   

def dedection(text: str) -> int:
    shift = evshift = 0
    while shift == 0:
        print(entschlüsselung_verschiebung(text, evshift))
        Eingabe = input("Ergibt das Sinn?")
        if Eingabe == "ja":
            shift = evshift
        else:
            evshift += 1    
    return shift

print(dedection("kdoor"))