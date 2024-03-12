import threading
import time
import math

def semifakultät(x, y):
    res = 1
    for i in range(x, y + 1):
        res *= i 
    return res 

def thread_fakultät(x, y, results, index): 
    results[index] = semifakultät(x, y)

def fakultät_multithreaded(n, t):
    threads = []
    result = 1
    results = [1 for i in range(t)]

    for index in range(t):
        x = threading.Thread(target=thread_fakultät, args=[n // t * index + 1, n // t * (index + 1), results, index])
        threads.append(x)
        x.start()

    for i in range(t):
        threads[i].join()
        result *= results[i]
    
    return result   

def thread_listensumme(liste, results):    
    results.append(sum(liste))

def listensumme_multithreaded(liste, t):
    summe = 0
    threads = []
    results = []

    for i in range(t - (len(liste) % t)):
        liste.append(0)

    listenlänge = len(liste)

    for index in range(t):
        x = threading.Thread(target=thread_listensumme, args=[liste[listenlänge // t * index:listenlänge // t * (index + 1)], results])
        threads.append(x)
        x.start()

    for i in range(t):
        threads[i].join()
        summe += results[i]

    return summe

def thread_max(liste, maxies):
    maxies.append(max(liste))

def max_multithreaded(liste, t): 
    threads = []
    maxies = []

    for i in range(t - (len(liste) % t)):
        liste.append(0) 

    listenlänge = len(liste)    

    for index in range(t):
        x = threading.Thread(target=thread_max, args=[liste[listenlänge // t * index:listenlänge // t * (index + 1)], maxies])
        threads.append(x)
        x.start()

    for i in range(t):
        threads[i].join()

    return max(maxies)

def thread_aufsteigendsortiert(liste, results, fe, le):
    results.append(liste == liste.sort())
    fe.append(liste[0])
    le.append(liste[-1])

def aufsteigendsortiert_multithreaded(liste, t):
    threads = []
    results = []
    fe = []
    le = []

    for i in range(t - (len(liste) % t)):
        liste.append(math.inf) 
    
    for index in range(t):
        x = threading.Thread(target=thread_aufsteigendsortiert, args=[liste[len(liste) // t * index:len(liste) // t * (index + 1)], results, fe, le])
        threads.append(x)
        x.start()

    fe.append(math.inf)

    for i in range(t):
        threads[i].join()
        if not results[i] or le[i] != fe[i + 1]:
            return False     

    return True

test = list(range(222222225))
start1 = time.time()

x = sum(test)          

time1 = time.time() - start1
start2 = time.time()

y = aufsteigendsortiert_multithreaded(test, 12)

time2 = time.time() - start2

print(time1, time2, x, y)        