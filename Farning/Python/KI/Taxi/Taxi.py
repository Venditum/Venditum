import numpy as np
import random
import copy

class Umwelt:
    def __init__(self, größe: tuple):
        self.field = np.zeros(größe)
        self.position = (random.randint(0, 4), random.randint(0, 4))
        self.passengerpositions = ([(random.randint(0, 4), random.randint(0, 4)) for i in range(4)])
        listcopy = copy.deepcopy(self.passengerpositions)
        self.passengerstart = listcopy.pop(random.randint(0, 3))
        self.passengerend = random.choice(listcopy)

e = Umwelt((5, 5))
print(e.field)
print(e.passengerpositions)
print(e.position)
print(e.passengerstart)
print(e.passengerend)