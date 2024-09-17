import csv, matplotlib.pyplot as plt, numpy as np
from mpl_toolkits import mplot3d

datensatz = []
with open("bmi.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

datensatz_nach_art = {}    
for zeile in datensatz:
    if zeile[-1] not in datensatz_nach_art:
        datensatz_nach_art[zeile[-1]] = []
    datensatz_nach_art[zeile[-1]].append(zeile[:-1])

#print(datensatz_nach_art)

def summe_fehlerquadrate(steigung, x_real, y_real):
    return sum((steigung * x - y) ** 2 for x in x_real for y in y_real)

def gradientenverfahren(x, y, repetitions):
    m = y[-1] / x[-1]
    a = 1
    onesided = True
    for i in range(repetitions):
        if summe_fehlerquadrate(m-a, x, y) < summe_fehlerquadrate(m, x, y):
            m -= a
        else:    
            m += a
            onesided = False
            a *= 0.8
            a = -a

    return m

x = list(i[0] for i in datensatz)
y = list(i[1] for i in datensatz)       

print(summe_fehlerquadrate(gradientenverfahren(x, y, 100), x, y))