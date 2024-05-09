import csv, matplotlib.pyplot as plt, numpy as np

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

datensatz_nach_art = {}    
for zeile in datensatz:
    if zeile[-1] not in datensatz_nach_art:
        datensatz_nach_art[zeile[-1]] = []
    datensatz_nach_art[zeile[-1]].append(zeile[:-1])  

def regressionsgerade(eingabe, x, y):
    m = sum([i * j for i in x for j in y]) / sum([i**2 for i in x]) / len(x)
    return m*eingabe

for art in datensatz_nach_art:
    y = [0, regressionsgerade(max([i[0] for i in datensatz_nach_art[art]]), [i[0] for i in datensatz_nach_art[art]], [i[1] for i in datensatz_nach_art[art]])]
    x = [0, max([i[0] for i in datensatz_nach_art[art]])]
    x_i = np.array([i[0] for i in datensatz_nach_art[art]])
    y_i = np.array([i[1] for i in datensatz_nach_art[art]])
    plt.plot(x, y)
    plt.scatter(x_i, y_i)
plt.show()