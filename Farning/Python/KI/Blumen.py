import csv
import math
import random
from tqdm import tqdm
import matplotlib.pyplot as plt

def euklidischer_abstand(zeile1, zeile2):
    a = 0
    for i in range(len(zeile2)):
        a += (zeile1[i] - zeile2[i])**2
    return math.sqrt(a)

def normalisieren(liste):
    maxi = max(liste)
    for i in range(len(liste)):
        i /= maxi

datensatz = []
with open("iris.csv") as f:
    csvreader = list(csv.reader(f))
    for zeile in csvreader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]]) 

datensatz_transponiert = list(zip(*datensatz))
maxima = []
for zeile in datensatz_transponiert:
    maxima.append(max(zeile))
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 2):
        datensatz[i][j] /= maxima[j]      

def generate_trainingsdata(p):
    random.shuffle(datensatz)
    trainings_flowers = datensatz[:int(len(datensatz) * p)]
    trainings_data = datensatz[int(len(datensatz) * p):]
    return trainings_flowers, trainings_data    

def predict(datensatz, probant, abstandvalue):
    distances_datensatz = []
    for zeile in datensatz:
        distances_datensatz.append((euklidischer_abstand(probant, zeile[:-1]), zeile[-1]))

    top_k = list(filter(lambda x: x[0] <= abstandvalue, distances_datensatz))    
    prediction = max([abstand[-1] for abstand in top_k], key= top_k.count) if len(top_k) > 0 else None

    return prediction

def evaluate(abstandvalue, trainings_tuple):
    korrekt = 0
    failed = 0
    for i in trainings_tuple[0]:
        prediction = predict(trainings_tuple[1], i, abstandvalue)
        if prediction == i[-1]:
            korrekt += 1
        if prediction == None:
            failed += 1    
    return korrekt / len(trainings_tuple[0]), failed / len(trainings_tuple[0])

def superevaluation(durchläufe, test_size, abstandvalue):
    total = 0
    for i in range(durchläufe):
        total += evaluate(abstandvalue, generate_trainingsdata(test_size))[0]
    return total / durchläufe    

def findoptimal(durchläufe, start, p, accuracy):
    abstandvalue = start
    for i in tqdm(range(durchläufe)):
        if superevaluation(100, p, abstandvalue + accuracy) > superevaluation(100, p, abstandvalue - accuracy):
            abstandvalue += accuracy
        else:
            abstandvalue -= accuracy
    return abstandvalue

def findoptimal2(durchläufe, p, kfaktor):
    accuracies = []
    for k in tqdm(range(durchläufe)):
        ks = (k / durchläufe) * kfaktor
        accuracies.append((ks, superevaluation(int(durchläufe // 2), p, ks)))
    return max(accuracies, key = lambda x: x[1])

def gewichtung(datensatz, ks, durchläufe):
    maxies = []
    for i in tqdm(range(1, ks)):
        for j in range(1, ks):
            for k in range(len(datensatz)):
                datensatz[k][2] *= i
                datensatz[k][3] *= j  
            plotsubject = findoptimal2(durchläufe, 0.2, 1)
            maxies.append((plotsubject, i, j))  
            for l in range(len(datensatz)):
                datensatz[l][2] /= i
                datensatz[l][3] /= j 

    return max(maxies)

for k in range(len(datensatz)):
    datensatz[k][2] *= 5
    datensatz[k][3] *= 3

print(gewichtung(datensatz, 3, 20))   