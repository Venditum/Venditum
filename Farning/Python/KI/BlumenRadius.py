import csv
import math

def euklidischer_abstand(p, q):
    a = 0
    for i in range(len(q)):
        a += (float(p[i]) - float(q[i]))**2
    return math.sqrt(a)

datensatz = []
with open("iris.csv") as f:
    datensatz = list(csv.reader(f))

test_datensatz = datensatz[0]

trainings_datensatz = datensatz[1:]

name_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

max_abstand = 2

top_k = []

distances_datensatz = []
for zeile in trainings_datensatz:
    distances_datensatz.append((euklidischer_abstand(test_datensatz, zeile[:-1]), zeile[-1]))

distances_datensatz.sort(key=lambda x : x[0])
top_k = list(filter(lambda x: x[0] <= max_abstand, distances_datensatz))    

prediction = max([abstand[-1] for abstand in top_k], key= top_k.count)
print(prediction)