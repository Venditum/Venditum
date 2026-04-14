import math
import random

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

def randomvalue():
    return random.choice([1, -1]) * random.random()

class Neuron:
    def __init__(self, weights: list, bias: float):
        self.weights = weights
        self.bias = [bias]
        self.value = 0

    def normalize(self, n: float) -> float:
        return 1 / (1 + math.e ** (-n))
    
    def activate(self, input):
        return self.normalize(mult([self.weights] ,inverse([input]))[0][0] + self.bias[0])

    def compute(self, inputs):
        self.value = self.activate(inputs)
    def cost(self, input, expected):
        return expected - self.activate(input)     

    def learnfunktion(self, input, expected):
        delta = scale([input], 0.1 * self.cost(input, expected))
        self.weights = add([self.weights], delta)[0]
        self.bias[0] += 0.1 * self.cost(input, expected)   

    def learn(self, datensatz, wiederholungen):
        for i in range(wiederholungen):
            for j in range(len(datensatz)):
                self.learnfunktion(datensatz[j][0], datensatz[j][1])

class Layer:
    def __init__(self, neurons: list):
        self.neurons = neurons
        self.weights = []
        for row in range(len(self.neurons)):
            self.weights.append(self.neurons[row].weights)
        self.bias = []
        for row in range(len(self.neurons)):
            self.bias.append(self.neurons[row].bias)    
     
    def getValues(self):
        values = []
        for neuron in self.neurons:
            values.append(neuron.value)
        return values

    def computevalues(self, inputLayer):
        for neuron in self.neurons:
            neuron.compute(inputLayer.getValues())  

    def getDelta(self, nextLayerWeights, nextLayerError):
        delta = mult(inverse(nextLayerWeights), nextLayerError)
        for row in range(len(delta)):
            val = self.getValues()[row]
            delta[row][0] *= val * (1 - val)
        return delta   

    def learnfunktion(self, inputLayer, nextLayerError, learnrate):
        self.weights = add(self.weights, scale(mult(nextLayerError, [inputLayer.getValues()]), learnrate))
        self.bias = add(self.bias, scale(nextLayerError, learnrate))
        for neuron in range(len(self.neurons)):
            self.neurons[neuron].weights = self.weights[neuron]
            self.neurons[neuron].bias = self.bias[neuron]


    def getError(self, expected):
        error = []
        for i in range(len(self.neurons)):
            error.append((expected[i] - self.getValues()[i]) * (self.getValues()[i] * (1 - self.getValues()[i])))
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
                    self.layers[0].neurons[neuron].value = trainingsdata[j][0][neuron]
                self.compute()
                nextLayerError = [self.layers[-1].getError(trainingsdata[j][1])]
                for layer in range(1, len(self.layers)):
                    current_layer = self.layers[-layer]
                    input_layer = self.layers[-(layer + 1)]
                    old_weights = current_layer.weights
                    current_layer.learnfunktion(input_layer, nextLayerError, 0.5)
                    if layer < len(self.layers) - 1:
                        nextLayerError = input_layer.getDelta(old_weights, nextLayerError)


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

inputNeuron1 = Neuron([], 0)
inputNeuron2 = Neuron([], 0)
hiddenNeuron1 = Neuron([randomvalue(), randomvalue()], randomvalue())
hiddenNeuron2 = Neuron([randomvalue(), randomvalue()], randomvalue())
hiddenNeuron3 = Neuron([randomvalue(), randomvalue()], randomvalue())
hiddenNeuron4 = Neuron([randomvalue(), randomvalue()], randomvalue())
hiddenLayer = Layer([hiddenNeuron1, hiddenNeuron2, hiddenNeuron3, hiddenNeuron4])
inputLayer = Layer([inputNeuron1, inputNeuron2])
endNeuron = Neuron([randomvalue(), randomvalue(), randomvalue(), randomvalue()], randomvalue())
endLayer = Layer([endNeuron])
network = Network([inputLayer, hiddenLayer, endLayer])
network.learn(10000, xor_datensatz)
inputNeuron1.value = 0
inputNeuron2.value = 1
network.compute()
print(endLayer.getValues())