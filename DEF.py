from _2021_11_09_funktionen import sortieren

def sortiert(liste):
    Vorherzahl = 0
    for zahl in liste:
        if zahl < Vorherzahl:
            return False
        else:
            Vorherzahl = zahl    
    return True        
        
liste = [1, 3, 4]  

index = 0
_2dex = 0
_3dex = 0
_4dex = 0
_5dex = 0
_6dex = 0
_7dex = 0
_8dex = 0
_9dex = 0
_10dex = 0
_11dex = 0
_12dex = 0
_13dex = 0
_14dex = 0
_15dex = 0
_16dex = 0
_17dex = 0
_18dex = 0
_1 = 10
_2 = 10
_3 = 1
_4 = 0
_5 = 1
_6 = 20
_7 = 5
_8 = 1

while index < 10:
    while _2dex < 10:
        #print("*", end="")
        _2dex += 1  
    index += 1
    _2dex = 0
    #print() 

while _3dex < 10: 
    while _4dex < _1:
        #print("*", end="")
        _4dex += 1
    #print()
    _3dex += 1 
    _1 -= 1  
    _4dex = 0 

while _5dex < 10:
    while _6dex < _2:
        #print(" " , end = "")
        _6dex += 1
    while _7dex < _3: 
        #print("*" , end="")
        _7dex += 1    
    print()
    _5dex += 1
    _6dex = 0
    _7dex = 0
    _2 -= 1
    _3 += 1

while _8dex < 20:
    while _9dex < _4:
        #print(" " , end = "")
        _9dex += 1
    while _10dex < _5:
        #print("*" , end = "")
        _10dex += 1
    while _11dex < _6:
        #print(" " , end = "")
        _11dex += 1
    while _12dex < _5:
        #print("*" , end = "")
        _12dex += 1
    while _13dex < _4:
        #print(" " , end = "")
        _13dex += 1
    #print()
    _8dex += 1
    _9dex = 0
    _10dex = 0
    _11dex = 0
    _12dex = 0
    _13dex = 0  
    if _8dex > 10:
        _4 -= 1
        _6 += 2 
    else:
        _4 += 1
        _6 -= 2

while _14dex < 11:
    while _15dex < _7:
        print(" " , end = "")
        _15dex += 1
    while _16dex < _8:
        print("*" , end = "")
        _16dex += 1
    while _17dex < _7:
        print(" " , end = "")
        _17dex += 1
    print()  
    _14dex += 1  
    _15dex = 0
    _16dex = 0
    _17dex = 0
    _7 -= 1
    _8 += 2