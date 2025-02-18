import csv

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
        self.b -= eta * (2 * (self.compute(_input) ** 2 - o))
        for i in range(len(self.w)):
            self.w[i] -= eta * (2 * (self.compute(_input) ** 2 - o)) * _input[i]

    def activate(self, _input):
        return self.compute(_input) > 0.5       

    def learn(self, eta, inputs, os, repetitions):
        for i in range(repetitions):
            for j in range(len(inputs)):
                self.singlelearn(eta, inputs[j], os[j])

a = adaline([0, 0, 0, 0], 0)
datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]])
os = []
for i in range(50):
    os.append(1)
for i in range(50):
    os.append(-1) 

a.learn(0.0000001, datensatz[:-50], os, 10000)   
print(datensatz)
print(a.w)
print(a.compute([4.8,3.4,1.6,0.2]))