#Fakultät

def fak(n: int) -> int:
    if n != 1:
        n *= fak(n - 1)
    return n     

print(fak(5))   


#Quersumme

def quersumme(n: int, n2: int) -> int:
    if len(zahl) == n - 1:
        exit()
    zahl = str(n)
    if len(zahl) != n - 2:
        zahl1 = int(zahl[n2]) + int(quersumme(int(zahl[n2 + 1]), n2 + 1))
    else:
        return zahl1
    return zahl1     

print(quersumme(55, 0))