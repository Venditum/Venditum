# eine for-Schleife, die alle Zahlen von 0 - 9 ausgibt

# for i in range(10):
#     print(i)
    
#Eine, die alle von 0 - 50 ausgibt    

# for i in range(51):
#     print(i)

#Eine, die alle von 10 - 25 ausgibt  

# for i in range(15):
#     print(i + 10)

#Eine von 50 - 150

# for i in range(100):
#     print(i + 50)

#Eine von 100 - 0

# z = 100
# for i in range(101):
#     print(i + z)
#     z -= 2

#Eine von 50 bis - 50

# z = 50
# for i in range(101):
#     print(i + z)
#     z -= 2

#Eine von 0 - 20 (2er Schritte)

# for i in range(11):
#     print(i * 2)

#Eine von 250 - 750(5er Schritte)

# for i in range(101):
#     print((i + 250) * 5)

#Eine von Quadratzahlen

# for i in range(20):
#     print(i ** 2)

#Eine mit 2er Potenzen

# for i in range(20):
#     print(2 ** i)

#Eine mit Liste(2er Potenzen)

# zw = 1
# liste = []
# for i in range(20):
#     liste.append(2 * zw)
#     zw *= 2
    
# print(liste)    

#zweidimensionale Listen

# liste = []

# for i in range(7):    
#     liste_zw = []
#     for z in range(i):
#        liste_zw.append(z)  
#     liste.append(liste_zw)
  
# liste = [] 

# for i in range(10):
#     liste_zw = []
#     for z in range(i):
#         liste_zw.append(i)
#     liste.append(liste_zw)  

# print(liste)

#Bauernhof

# Beine = 94
# Kaninchen = 0
# Hühner = 0
# x = 34

# for i in range(x):
#     while (Beine - 4) >= 0:
#         Kaninchen += 1
#         Beine -= 4
#     x -= Kaninchen
#     while x > 0:
#         Kaninchen -= 1
#         Hühner += 2
#         x -= 1
#     while (Beine - 2) >= 0:
#         Hühner += 1
#         Beine -= 2    

# print(Kaninchen)     
# print(Hühner)   

<<<<<<< Updated upstream
def bauernhof(köpfe: int, beine: int, dict_beine: dict):
    for i in bauernhof(köpfe, beine, dict_beine):
        for e in bauernhof(köpfe, beine, dict_beine):
            if e + i == köpfe and i * 4 + e * 2 == beine:
                print(e, i)

print(bauernhof(10, 10, {"Igel": 4, "Ente": 2}))    
=======
def bauernhof(köpfe: int, beine: int, dict_beine: dict) -> dict:
    dict_tiere = dict_beine
    x = len(dict_beine)  
    for tiere in range(len(dict_tiere)):
        key = dict_tiere.popitem()
        for x in range(köpfe):
            
            
print(bauernhof(10, 20, {"Igel": 4, "Ente": 2}))    
>>>>>>> Stashed changes
