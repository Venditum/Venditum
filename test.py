def verschlüsselung(text):
    Buchstabe = 0
    while Buchstabe < 5: 
        zwa = ord(text[Buchstabe])
        ord(text[Buchstabe])
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
        print(za, end= "")
        Buchstabe += 1

verschlüsselung("hallo")     