import threading
import time
import math
import multiprocessing

def listen_teiler(liste, n):
    if n <= 0:
        raise ValueError("n nicht positiv")
    liste_von_teillisten = [[]] * n
    for i in range(len(liste)):
        liste_von_teillisten[i % n].append(liste[i])
    return liste_von_teillisten 

def listen_teiler2(liste, n): 
    if n <= 0:
        raise ValueError("n nicht positiv")
    liste_von_teillisten = [[]] * n
    list_indizes = [[len(liste) // n * i, len(liste) // n * (i + 1)] for i in range(n)]
    list_indizes[-1][-1] = -1
    for i in range(n): 
        liste_von_teillisten[i] = liste[list_indizes[i][0]:list_indizes[i][1]] 
    return liste_von_teillisten    
                

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
        x = threading.Thread(target=thread_max, args=[liste[len(liste) // t * index:len(liste) // t * (index + 1)], maxies])
        threads.append(x)
        x.start()

    for i in range(t):
        threads[i].join()

    return max(maxies)

def thread_aufsteigendsortiert(liste, results, fe, le):
    results.append(sorted(liste))
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
        if not results[i] or le[i] > fe[i + 1]:
            return False     

    return True

def max_single(liste):
    max = -math.inf
    for i in liste:
        if i > max:
            max = i
    return max

def maximum_multi(liste, k):
    list_indizes = [[len(liste) // k * i, len(liste) // k * (i + 1)]for i in range(k)]
    list_indizes[-1][-1] = -1

    with multiprocessing.Pool(k) as pool:
        liste_geteilt = listen_teiler2(liste, k)    
        ergebnisse = pool.map(max, liste_geteilt)   

    return max_single(ergebnisse)     

if __name__ == "__main__":

    zufallsliste = [i for i in range(20000000)]

    t1 = time.time()
    maximum_multi(zufallsliste, 8)
    print(time.time() - t1)

    t1 = time.time()
    max(zufallsliste)
    print(time.time() - t1)

# test = list(range(22))
# start1 = time.time()

# x = sum(test)          

# time1 = time.time() - start1
# start2 = time.time()

# y = aufsteigendsortiert_multithreaded(test, 12)

# time2 = time.time() - start2

# print(time1, time2, x, y)        