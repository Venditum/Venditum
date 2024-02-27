import logging
import threading
import time
import concurrent.futures

def semifakultät(x, y):
    if y == 0:
        return 1
    t = 1
    for i in range(x, y):
        t *= (i + 1)
    return t  

def thread_function(semifakultät): 
    logging.info("Thread %s: starting", semifakultät)
    time.sleep(2)
    logging.info("Thread %s: finishing", semifakultät)    
def fakultät_multithreaded(n, t):
    fakultäten = []
    fakultät = 1
    threads_number = t  
   
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(t):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(int(t / (index + 1)), int(t / (index + 2))))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    
    return fakultät  

print(fakultät_multithreaded(10, 5))