import csv
import math

def euklidischer_abstand(p, q):
    a = 0
    for i in range(len(q)):
        a += (float(p[i]) - float(q[i]))**2
    return math.sqrt(a)

def read_lines():
    with open("iris.csv") as f:
        datensatz = list(csv.reader(f))
        for row in datensatz:
            yield [float(i) for i in row[:-1]]

datensatz = list(read_lines())

print(datensatz)

test_datensatz = datensatz[0]

trainings_datensatz = datensatz[1:]

name_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

k = 10

distances_datensatz = []
for zeile in trainings_datensatz:
    distances_datensatz.append((euklidischer_abstand(test_datensatz, zeile[:-1]), zeile[-1]))

distances_datensatz.sort(key=lambda x : x[0])
top_k = distances_datensatz[:k]

prediction = max([abstand[-1] for abstand in top_k], key= top_k.count)

print(prediction)

def normalisieren_datensatz(liste):
    new_list = []
    maxwerte = []
    for i in liste:
        maxwerte.append(max(i))
    maxi = max(maxwerte) 
    print(maxi)
    for i in liste:
        y = []
        new_list.append(y)
        for x in i:
            new = x / maxi
            y.append(new)
    return new_list        
print(normalisieren_datensatz(datensatz))
