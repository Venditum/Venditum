import math

#Fakultät

def fak(n: int) -> int:
    if n == 0:
        return 1
    return n * fak(n - 1)       

#Quersumme

def quersumme(n: int) -> int:
    n_str = str(n)
    if len(n_str) == 1:
        return n
    vorgänger = int(n_str[1:])
    quersumme_vorgänger = quersumme(vorgänger)
    quersumme_n = int(n_str[0]) + quersumme_vorgänger
    return quersumme_n    

#Quersumme2

def quersumme_a(n: int) -> int:
    if n < 10:
        return n
    vorgänger = (n - (n % 10)) / 10 
    quersumme_vorgänger = quersumme_a(vorgänger)
    return (n % 10) + quersumme_vorgänger

#V_Q

def V_Q(zahl: int, verdoppeln: bool) -> int:
    if zahl >= 1000000:
        return zahl 
    elif verdoppeln:
        zahl *= 2
        return V_Q(zahl, False)   
    else: 
        zahl *= 2
        return V_Q(zahl, True)     

def V_Q_(zahl: int) -> int:
    return V_Q(zahl, True)    

#V_Q_alt

def V_Q_alt(zahl: int, verdoppeln: bool, anzahl: int) -> int:
    if zahl >= 1000000:
        return anzahl
    elif verdoppeln:
        zahl *= 2
        return V_Q_alt_(zahl, False, anzahl + 1)   
    else: 
        zahl *= 2
        return V_Q_alt_(zahl, True, anzahl + 1) 

def V_Q_alt_(zahl: int) -> int:
    return V_Q_alt(zahl, True, 0)            

#optimum

<<<<<<< Updated upstream
def optimum(list: list[int]) -> int:
    best = -math.inf
    best_i = -1
    for i in range(len(list)):
        original = list[i]
        list[i] = 0
        lb = ...
        list[i] = original
        if lb > best:
            best = lb
            best_i = i
    return best_i        
=======
print(quersumme_a(24))        
>>>>>>> Stashed changes
