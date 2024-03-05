import threading
import time

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
        x = threading.Thread(target=thread_function, args=[n // t * index + 1, n // t * (index + 1), results, index])
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
    listenlänge = len(liste)

    for index in range(t - 1):
        x = threading.Thread(target=thread_listensumme, args=[liste[listenlänge // t * index:listenlänge // t * (index + 1)], results])
        threads.append(x)
        x.start()

    for i in range(t - 1):
        threads[i].join()
        summe += results[i]

    return summe + sum(liste[listenlänge // t * (t - 1):])

def thread_max(liste, maxies):
    maxies.append(max(liste))

def max_multithreaded(liste, t): 
    threads = []
    maxies = []
    listenlänge = len(liste)

    for index in range(t - 1):
        x = threading.Thread(target=thread_max, args=[liste[listenlänge // t * index:listenlänge // t * (index + 1)], maxies])
        threads.append(x)
        x.start()

    for i in range(t - 1):
        threads[i].join()

    return max([max(maxies), max(liste[listenlänge // t * (t - 1):])])

test = list(range(222222225))
start1 = time.time()

x = max(test)          

time1 = time.time() - start1
start2 = time.time()

y = max_multithreaded(test, 12)

time2 = time.time() - start2

print(time1, time2, x, y)        