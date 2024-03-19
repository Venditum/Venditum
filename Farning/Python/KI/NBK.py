import csv, matplotlib.pyplot as plt

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

arten = {}
for i in range(len(datensatz)):
    if not datensatz[i][-1] in arten:
        arten[datensatz[i][-1]] = []       
    arten[datensatz[i][-1]].append(datensatz[i])

print(arten)