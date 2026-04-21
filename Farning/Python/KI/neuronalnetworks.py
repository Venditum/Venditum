import math
import random
import copy
import csv

def add(A, B):
    result = []
    for row in range(len(A)):
        newrow = []
        for column in range(len(A[0])):
            newrow.append(A[row][column] + B[row][column])
        result.append(newrow)
    return result   
 
def scale(A, scalar):
    result = []
    for row in range(len(A)):
        newrow = []
        for column in range(len(A[0])):
            newrow.append(A[row][column] * scalar)
        result.append(newrow)
    return result  

def mult(A, B):
    if len(B) == 1 and len(B[0]) == 1:
        return scale(A, B[0][0])
    if len(A) == 1 and len(A[0]) == 1:
        return scale(B, A[0][0])
    result = []
    for row in range(len(A)):
        newrow = []
        for columm in range(len(B[0])):
            newvalue = 0
            for Avalue in range(len(A[row])):
                newvalue += A[row][Avalue] * B[Avalue][columm]
            newrow.append(newvalue)
        result.append(newrow)
    return result   

def inverse(A):
    result = []
    for column in range(len(A[0])):
        newrow = []
        for row in range(len(A)):
            newrow.append(A[row][column])
        result.append(newrow)
    return result   

def functionforMatrix(A, function):
    for row in range(len(A)):
        for column in range(len(A[0])):
            A[row][column] = function(A[row][column])

def sigmoid(n):
    return 1 / (1 + math.e ** (-n))  

def derivsigmoid(n):
    return n * (1 - n)

def leakyreLU(n):
    return n if n >= 0 else 0.01 * n

def derivleakyreLU(n):
    return 1 if n >= 0 else 0.01 

def randomvalue():
    return random.choice([1, -1]) * random.random()

class InputLayer:
    def __init__(self, values):
        self.values = values

class Layer:
    def __init__(self, neurons, neuronsinput):
        self.weights = []
        self.bias = []
        self.values = [] 
        for neuron in range(neurons):
            row = []
            for weight in range(neuronsinput):
                row.append(randomvalue())
            self.weights.append(row)    
            self.bias.append([randomvalue()]) 
            self.values.append([0])

    def computevalues(self, values, function):
        self.values = add(mult(self.weights, values), self.bias)
        functionforMatrix(self.values, function)

    def getDelta(self, nextLayerWeights, nextLayerError, function):
        delta = mult(inverse(nextLayerWeights), nextLayerError)
        values = copy.deepcopy(self.values)
        functionforMatrix(values, function) 
        for row in range(len(delta)):
            delta[row][0] *= values[row][0]
        return delta   

    def learnfunktion(self, inputLayer, nextLayerError, learnrate):
        self.weights = add(self.weights, scale(mult(nextLayerError, inverse(inputLayer.values)), learnrate))
        self.bias = add(self.bias, scale(nextLayerError, learnrate))

    def getError(self, expected, function):
        target = [[x] for x in expected]
        diff = add(target, scale(self.values, -1))
        deriv = copy.deepcopy(self.values)
        functionforMatrix(deriv, function) 
        for row in range(len(diff)):
            diff[row][0] *= deriv[row][0]
        return diff

class Network:
    def __init__(self, architecture):
        self.layers = []
        for i in range(len(architecture)):
            self.layers.append(Layer(architecture[i][0], architecture[i][1]))

    def compute(self, values):
        function = leakyreLU
        for i in range(len(self.layers)):
            if i == len(self.layers) - 1:
                function = sigmoid
            if i == 0:
                self.layers[i].computevalues(values, function)  
            else:
                self.layers[i].computevalues(self.layers[i - 1].values, function)    

    def learn(self, repetitions, trainingsdata):
        for i in range(repetitions):
            for j in range(len(trainingsdata)):
                self.compute(inverse([trainingsdata[j][0]]))
                currentError = self.layers[-1].getError(trainingsdata[j][1], derivsigmoid)
                for layer in range(len(self.layers) - 1, -1, -1):
                    current_layer = self.layers[layer]
                    if layer > 0:
                        input_layer = self.layers[layer-1]
                    else:
                        input_layer = InputLayer(inverse([trainingsdata[j][0]]))
                    if layer > 0:
                        delta = input_layer.getDelta(current_layer.weights, currentError, derivleakyreLU)
                    current_layer.learnfunktion(input_layer, currentError, 0.4)
                    currentError = delta


xor_datensatz = [
    [[0, 0], [0]],
    [[0, 1], [1]],
    [[1, 0], [1]],
    [[1, 1], [0]]
]

and_datensatz = [
    [[0, 0], 0],
    [[0, 1], 0],
    [[1, 0], 0],
    [[1, 1], 1]
]

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

expectedvalues = []
for i in range(50):
    expectedvalues.append([1, 0, 0])   

for i in range(50):
    expectedvalues.append([0, 1, 0])   

for i in range(50):
    expectedvalues.append([0, 0, 1])

iris_training = []    

for i in range(150):
    iris_training.append([datensatz[i][:-1], expectedvalues[i]])

network = Network([[10, 4], [10, 10], [10, 10], [3, 10]])
network.learn(5000, iris_training)
network.compute(inverse([[5.1,3.5,1.4,0.2]]))
print(network.layers[-1].values)
network.compute(inverse([[4.5,2.3,1.3,0.3]]))
print(network.layers[-1].values)
network.compute(inverse([[6.6,3.0,4.4,1.4]]))
print(network.layers[-1].values)
network.compute(inverse([[5.7,2.9,4.2,1.3]]))
print(network.layers[-1].values)
network.compute(inverse([[6.8,3.2,5.9,2.3]]))
print(network.layers[-1].values)
network.compute(inverse([[7.2,3.0,5.8,1.6]]))
print(network.layers[-1].values)

#network.compute()
#print(endLayer.getValues())