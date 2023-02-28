print("Hallo und willkommen zum Zahlenraten!")
spieler1 = input("Wie heißt du, Spieler1? ")
spieler2 = input("Wie heißt du, Spieler2? ")
listespieler = [spieler1, spieler2]
spielfertig = False

while True:
    for spieler in listespieler:
        versuch = 0
        Geheimzahl = int(input("bitte wegschauen, " + spieler + ", während dein Mitspieler die Geheimzahl angibt "))
        while versuch <= 10:
            geheimzahlversuch = int(input(spieler + " Bitte versuche, die Zahl zu erraten! "))
            if geheimzahlversuch > Geheimzahl:
                if Geheimzahl / geheimzahlversuch >= 0.8:
                    if Geheimzahl / geheimzahlversuch >= 0.97:
                        print("Noch ganz bisschen kleiner")
                    print("Es war nah dran, die Zahl ist bisschen kleiner!")
                else:
                    print("Die Zahl ist kleiner") 
                print("Du hast noch " + str(10 - versuch) + " Versuche")
                versuch += 1       
            elif geheimzahlversuch < Geheimzahl:
                if geheimzahlversuch / Geheimzahl >= 0.8:
                    if geheimzahlversuch / Geheimzahl >= 0.97:
                        print("Noch ganz bisschen größer")
                    print("Es war nah dran, die Zahl ist bisschen größer!")
                else:
                    print("Die Zahl ist größer") 
                print("Du hast noch " + str(10 - versuch) + " Versuche")
                versuch += 1           
            else:
                print("Herzlichen Glückwunsch " + spieler)
                break
        if input("Möchtet ihr weiterspielen ") != "Ja":
            exit("Vielen Dank für das Spielen!")    