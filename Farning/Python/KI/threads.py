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

def thread_listensumme(liste, x, y, results, index):    
    results[index] = sum(liste[x:y])

def listensumme_multithreaded(liste, t):
    summe = 0
    threads = []
    results = [0 for i in range(t)]

    for index in range(t):
        x = threading.Thread(target=thread_listensumme, args=[liste, len(liste) // t * index, len(liste) // t * (index + 1), results, index])
        threads.append(x)
        x.start()

    for i in range(t):
        threads[i].join()
        summe += results[i]

    return summe

test = range(2222222222)
start1 = time.time()

x = sum(test)          

time1 = time.time() - start1
start2 = time.time()

y = listensumme_multithreaded(test, 8)

time2 = time.time() - start2

print(time1, time2, x, y)