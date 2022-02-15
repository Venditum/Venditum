def verschlüsselung(text):
    Buchstabe = 0
    ergebnis = ""
    while Buchstabe < len(text): 
        zwa = ord(text[Buchstabe])
        ord(text[Buchstabe])
        if zwa >= 117:
            zwa -= 5
        else:
            zwa += 5
        za = chr(zwa)
        if za == "a":
            za = "00001"  
        if za == "b":
            za = "00010"
        if za == "c":
            za = "00011" 
        if za == "d":
            za = "00100"  
        if za == "e":
            za = "00101"
        if za == "f":
            za = "00110"     
        if za == "g":
            za = "00111"  
        if za == "h":
            za = "01000"
        if za == "i":
            za = "01001"  
        if za == "j":
            za = "01010"  
        if za == "k":
            za = "01011"
        if za == "l":
            za = "01100" 
        if za == "m":
            za = "01101"  
        if za == "n":
            za = "01110"
        if za == "o":
            za = "01111"     
        if za == "p":
            za = "10000"  
        if za == "q":
            za = "10001"
        if za == "r":
            za = "10010"
        if za == "s":
            za = "10011"  
        if za == "t":
            za = "10100"
        if za == "u":
            za = "10101" 
        if za == "v":
            za = "10110"  
        if za == "w":
            za = "10111"
        if za == "x":
            za = "11000"     
        if za == "y":
            za = "11001"  
        if za == "z":
            za = "11010"
        if za == ".":
            za = "11011"
        if za == ",":
            za = "11100"
        if za == "?":
            za = "11101"
        if za == "!":
            za = "11110"
        if za == ":":
            za = "11111"   
        if za == " ":
            za = "00000"         
        ergebnis += za
        Buchstabe += 1
    print(ergebnis)

def entschlüsselung(text):
    Buchstabe = 0
    Buchstabe1 = 1
    Buchstabe2 = 2
    Buchstabe3 = 3
    Buchstabe4 = 4
    endbuch = ""
    ergebnis = ""
    while Buchstabe < len(text): 
        za = Buchstabe
        zb = text[za]
        if zb == "00001":
            endbuch = "a"  
        if zb == "00010":
            endbuch = "b"
        if zb == "00011":
            endbuch = "c" 
        if zb == "00100":
            endbuch = "d"  
        if zb == "00101":
            endbuch = "e"
        if zb == "00110":
            endbuch = "f"     
        if zb == "00111":
            endbuch = "g"  
        if zb == "01000":
            endbuch = "h"
        if zb == "01001":
            endbuch = "i"  
        if zb == "01010":
            endbuch = "j"  
        if zb == "01011":
            endbuch = "k"
        if zb == "01100":
            endbuch = "l" 
        if zb == "01101":
            endbuch = "m"  
        if zb == "01110":
            endbuch = "n"
        if zb == "01111":
            endbuch = "o"     
        if zb == "10000":
            endbuch = "p"  
        if zb == "10001":
            endbuch = "q"
        if zb == "10010":
            endbuch = "r"
        if zb == "10011":
            endbuch = "s"  
        if zb == "10100":
            endbuch = "t"
        if zb == "10101":
            endbuch = "u" 
        if zb == "10110":
            endbuch = "v"  
        if zb == "10111":
            endbuch = "w"
        if zb == "11000":
            endbuch = "x"     
        if zb == "11001":
            endbuch = "y"  
        if zb == "11010":
            endbuch = "z"
        if za == ".":
            za = "11011"
        if za == ",":
            za = "11100"
        if za == "?":
            za = "11101"
        if za == "!":
            za = "11110"
        if za == ":":
            za = "11111"   
        if za == " ":
            za = "00000" 
        ord(text[Buchstabe])
        zwa = ord(text[Buchstabe])
        if zwa >= 117:
            zwa += 5
        else:
            zwa -= 5            
        ergebnis += endbuch
        Buchstabe += 5    
    print(ergebnis)  

verschlüsselung("hallo")
entschlüsselung("0110100110100011000110100")

