import math
import csv
import numpy as np

def perceptron(perceptronin: list, m:list, b):
    result = 0
    for i in range(len(perceptronin)):
        result += perceptronin[i] * m[i]   
    return result + b > 0

def convert(bool):
    return 1 if bool else 0

case1 = [1, 1]
case2 = [0, 0]
case3 = [0, 1]
case4 = [1, 0]
Datensatz = [[case1, 1], [case2, 0], [case3, 0], [case4, 0]]
b = 0
def andlearn(Datensatz, b):
    m = [0, 0]
    for i in range(100):
        for element in Datensatz:
            actual = convert(perceptron(element[0], m, b))
            m[0] += (element[1] - actual) * element[0][0] 
            m[1] += (element[1] - actual) * element[0][1]
            b += element[1] - actual
    # print(convert(perceptron(true1, m, b)))
    # print(m)
    print(perceptron(Datensatz[0][0], m, b))
    print(perceptron(Datensatz[1][0], m, b))
    print(perceptron(Datensatz[2][0], m, b))
    print(perceptron(Datensatz[3][0], m, b))
    print(b)
    return m, b

#print(andlearn(Datensatz, b))     
#print(perceptron(case3, [0, -9], 10))

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

datensatz_transposed = [[],[],[],[]]

for i in range(4):
    for zeile in datensatz:
        datensatz_transposed[i].append(zeile[i])      

for i in range(4):
    for j in range(150):
        datensatz_transposed[i][j] = datensatz_transposed[i][j] / max(datensatz_transposed[i])

for i in range(4):
    for j in range(150):   
        datensatz[j][i] = round(datensatz_transposed[i][j], 4)           

expected = []
for i in range(50):
    expected.append([1, 0, 0])   

for i in range(50):
    expected.append([0, 1, 0])   

for i in range(50):
    expected.append([0, 0, 1])      

class Neuron:
    def __init__(self, weights: list, bias: float):
        self.weights = weights
        self.bias = bias
        self.value = 0

    def normalize(self, n: float) -> float:
        if n <= 0:
            return 0
        if n >= 1:
            return 1
        return n    

    def compute(self, inputs):
        output = 0
        for i in range(len(inputs)):
            output += inputs[i] * self.weights[i]
        self.value = self.normalize(output + self.bias) 

    def cost(self, expected):
        return expected - self.value     

    def learn(self, expected):
        for i in range(len(self.weights)):
            self.weights[i] += self.weights[i] * self.cost(expected) * 0.1

class Layer:
    def __init__(self, neurons: list):
        self.neurons = neurons
        self.values = []
        for neuron in neurons:
            self.values.append(-1)

    def compute_values(self, inputLayer):
        for i in range(len(self.neurons)):
            self.neurons[i].compute(inputLayer.values)
            self.values[i] = self.neurons[i].value

    def cost(self, expected):
        out = 0
        for i in range(len(self.neurons)):
            out += (self.neurons[i].value - expected[i]) ** 2
        return out    

    def learn(self, expected):
        for i in range(len(self.neurons)):
            self.neurons[i].learn(expected[i])

class Network:
    def __init__(self, layers: list):
        self.layers = layers
        self.endvalues = layers[-1].values

    def compute(self, values):
        self.layers[0].values = values
        for i in range(1, len(self.layers)):
            self.layers[i].compute_values(self.layers[i - 1])

    def learn(self, trainingsdata, expected):
        for i in range(len(trainingsdata)):
            self.compute(trainingsdata[i][:-1])
            exp = expected[i]
            for j in range(1, len(self.layers)):
                print(exp)
                self.layers[-j].learn(exp)
                exp = self.layers[-j].values


layer0 = Layer([])
layer1 = Layer([Neuron([0.1, 0.1, 0.1, 0.1], 0), Neuron([0.1, 0.1, 0.1, 0.1], 0), Neuron([0.1, 0.1, 0.1, 0.1], 0), Neuron([0.1, 0.1, 0.1, 0.1], 0)])
endlayer = Layer([Neuron([0.1, 0.1, 0.1, 0.1], 0), Neuron([0.1, 0.1, 0.1, 0.1], 0), Neuron([0.1, 0.1, 0.1, 0.1], 0)])          
network = Network([layer0, layer1, endlayer])
network.compute([0.6456, 0.7955, 0.2029, 0.08])
network.learn(datensatz, expected)
print(network.endvalues)