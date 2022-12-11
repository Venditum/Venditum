print("Wilkommen zu DEM Taschenrechner")
erste_zahl = float(input("Gib deine erste Zahl ein: "))
zweite_zahl = float(input("Gib deine Zweite Zahl ein: "))
operation = input("Was möchtest du machen: ")

def mal(n1:float, n2:float) -> float:
    return n1 * n2
def geteilt(n1:float, n2:float) -> float:
    return n1 / n2
def minus(n1:float, n2:float) -> float:
    return n1 - n2
def plus(n1:float, n2:float) -> float:
    return n1 + n2

if operation == "+":
    ergebnis = plus(erste_zahl, zweite_zahl)   
if operation == "*": 
    ergebnis = mal(erste_zahl, zweite_zahl)
if operation == "-": 
    ergebnis = minus(erste_zahl, zweite_zahl)
if operation == "/":  
    ergebnis = geteilt(erste_zahl, zweite_zahl)

print(ergebnis)
def fortsetzen():
    zweite_zahl = float(input("Gib deine Zahl ein: "))
    operation = input("Was möchtest du machen: ")
    if operation == "+":
        ergebnis = plus(erste_zahl, zweite_zahl)   
    if operation == "*": 
        ergebnis = mal(erste_zahl, zweite_zahl)
    if operation == "-": 
        ergebnis = minus(erste_zahl, zweite_zahl)
    if operation == "/":  
        ergebnis = geteilt(erste_zahl, zweite_zahl)
    return ergebnis    
eingabe = input("reset oder fortsetzen: ")
while eingabe != "reset":
    if eingabe == "fortsetzen":
        ergebnis = fortsetzen()
        print(ergebnis)
ergebnis = 0       