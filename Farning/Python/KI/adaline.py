import csv
import random
import matplotlib.pyplot as plt

class adaline:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def compute(self, _input):
        result = 0
        for i in range(len(self.w)):
            result += _input[i] * self.w[i]   
        return result + self.b

    def singlelearn(self, eta, _input, o):
        self.b -= eta * (2 * ((self.compute(_input) - o)))  
        for i in range(len(self.w)):
            self.w[i] -= eta * (2 * ((self.compute(_input) - o))) * _input[i]
    
    def activate(self, _input):
        return self.compute(_input) > 0       

    def learn(self, inputs, os, repetitions):
        for i in range(repetitions):
            rand_a = random.randint(0, len(inputs) // 2 - 1)
            rand_b = random.randint(len(inputs) // 2, len(inputs))
            for j in range(rand_b - rand_a):
                self.singlelearn((self.compute(inputs[j]) - os[j]) ** 2 / 1000, datensatz[j], os[j])     
        

a = adaline([0, 0], 0)
datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[2:-1]])
os = []
for i in range(50):
    os.append(1)
for i in range(100):
    os.append(-1) 

print(datensatz)
a.learn(datensatz, os, 10000)   
print(a.w)
print(a.activate([1.6,0.2])) # yes
print(a.compute([1.6,0.2])) # yes
print(a.activate([4.7,1.4])) # no
print(a.compute([4.7,1.4])) # no
print(a.activate([6.0,2.5])) # no
print(a.compute([6.0,2.5])) # no
print(a.plot(datensatz))