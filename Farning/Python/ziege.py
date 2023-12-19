import random

ja = 0
nein = 0
for i in range(1000):
    a = random.randint(0, 2)
    b = 2
    if a == b:
        b = random.choice([2, 1])
        if b == 1:
            b = random.choice([2, 0])
        else:
            b = random.choice([2, 1])    
    if a == 1:
        b = random.choice([1, 2])
    if a == 0:
        b = random.choice([0, 2])  
    if b == a:
        ja += 1

print(ja)