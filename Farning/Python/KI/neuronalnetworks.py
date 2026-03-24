import math

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
     
A = [[1, 5], [4, 5]]
B = [[7], [2]]
C = [[7], [2]]

print(mult(A, B))
print(inverse(B))
print(add(B, C))


class Neuron:
    def __init__(self, weights: list, bias: float):
        self.weights = inverse([weights])
        self.bias = bias
        self.value = 0

    def normalize(self, n: float) -> float:
        return 1 / (1 + math.e ** (-n))
    
    def activate(self, input):
        return self.normalize(mult([input], self.weights)[0][0] + self.bias)

    def compute(self, inputs):
        self.value = self.activate(inputs)
    def cost(self, input, expected):
        return expected - self.activate(input)     

    def learnfunktion(self, input, expected):
        delta = scale(inverse([input]), 0.1 * self.cost(input, expected))
        self.weights = add(self.weights, delta)
        self.bias += 0.1 * self.cost(input, expected)   

    def learn(self, datensatz, wiederholungen):
        for i in range(wiederholungen):
            for j in range(len(datensatz)):
                self.learnfunktion(datensatz[j][0], datensatz[j][1])

class Layer:
    def __init__(self, neurons: list):
        self.neurons = neurons
        self.weights = []
        for row in range(len(self.neurons)):
            weights = []
            for weight in self.neurons[row].weights:
                weights.append(weight)
        self.weights = inverse(self.weights)        
    
    def getValues(self):
        values = []
        for neuron in self.neurons:
            values.append(neuron.value)
        return values

    def computevalues(self, inputLayer):
        for neuron in self.neurons:
            neuron.compute(inputLayer.getValues())  

    def getDeltas(self, nextLayerError, nextLayerNeurons):
        


    def learnfunktion(self, inputLayer, nextLayerError, learnrate, nextLayerNeurons):
        for neuron in range(len(self.neurons)):
            for i in range(len(self.neurons[neuron].weights)):
                self.neurons[neuron].weights[i] += learnrate * self.getDeltas(nextLayerError, nextLayerNeurons)[neuron] * inputLayer.neurons[i].value     
            self.neurons[neuron].bias += learnrate * self.getDeltas(nextLayerError, nextLayerNeurons)[neuron]    

    def getError(self, expected):
        error = []
        for i in range(len(self.neurons)):
            error.append(expected[i] - self.getValues()[i])
        return error

class Network:
    def __init__(self, layers: list):
        self.layers = layers

    def compute(self):
        for i in range(1, len(self.layers)):
            self.layers[i].computevalues(self.layers[i - 1])  

    def learn(self, repetitions, trainingsdata):
        for i in range(repetitions):
            for j in range(len(trainingsdata)):
                for neuron in range(len(self.layers[0].neurons)):
                    for k in range(len(trainingsdata[0][0])):
                        self.layers[0].neurons[neuron].value = trainingsdata[j][0][k]
                self.compute()
                nextLayerError = self.layers[-1].getError(trainingsdata[j][1])
                for layer in range(1, len(self.layers)):
                    print(1)
                    print(len(self.layers[-layer].neurons))
                    self.layers[-layer].learnfunktion(self.layers[-(layer + 1)], nextLayerError, 0.1, len(self.layers[-layer].neurons))
                    nextLayerError = self.layers[-layer].getDeltas(nextLayerError, len(self.layers[-layer].neurons))     

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

Neuro = Neuron([0, 0], 0)
Neuro.learn(and_datensatz, 1000)
Neuro.compute([1, 0])
print(Neuro.value)
# inputNeuron1 = Neuron([], 0)
# inputNeuron2 = Neuron([], 0)
# inputNeuron1.value = 1
# inputNeuron2.value = 1
# hiddenNeuron1 = Neuron([0, 0], 0)
# hiddenNeuron2 = Neuron([0, 0], 0)
# inputLayer = Layer([inputNeuron1, inputNeuron2])
# hiddenLayer = Layer([hiddenNeuron1, hiddenNeuron2])
# endNeuron = Neuron([0, 0], 0)
# endLayer = Layer([endNeuron])
# network = Network([inputLayer, hiddenLayer, endLayer])
# inputNeuron1.value = 1
# inputNeuron2.value = 0