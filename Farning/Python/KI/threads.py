import threading
import time

def semifakultät(x, y):
    res = 1
    for i in range(x, y + 1):
        res *= i 
    return res 

def thread_function(x, y, results, index): 
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

start = time.time()
fakultät_multithreaded(200000, 1)
print(time.time() - start)