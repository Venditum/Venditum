import csv
import math

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

def predict(datensatz, probant, abstandvalue):
    distances_datensatz = []
    for zeile in datensatz:
        distances_datensatz.append((euklidischer_abstand(probant, zeile[:-1]), zeile[-1]))

    top_k = list(filter(lambda x: x[0] <= abstandvalue, distances_datensatz))    
    prediction = max([abstand[-1] for abstand in top_k], key= top_k.count)

    return prediction

def evaluate(abstandvalue):
    korrekt = 0
    for i in datensatz:
        if predict(datensatz, i, abstandvalue) == i[-1]:
            korrekt += 1
    return korrekt / len(datensatz)

print(evaluate(0.05))