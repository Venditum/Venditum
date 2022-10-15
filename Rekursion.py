#Fakultät

def fak(n: int) -> int:
    if n != 1:
        n *= fak(n - 1)
    return n       

#Quersumme

def quersumme(n: int, n2: int) -> int:
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

def V_Q(x):
    if x >= 1000000:
        return x 
    nachfolger = V_Q(x * 2)
    return nachfolger ** 2

print(V_Q(50))        