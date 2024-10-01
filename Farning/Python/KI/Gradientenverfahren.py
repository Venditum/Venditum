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
    return sum((steigung * x_real[i] - y_real[i]) ** 2 for i in range(len(x_real)))

def summe_fehlerquadrate_ableitung(steigung, x_real, y_real):
    return sum(2 * (steigung*x_real[i] - y_real[i]) * x_real[i] for i in range(len(x_real)))

def gradientenverfahren(x, y, repetitions):
    m = y[-1] / x[-1]
    a = 2
    for i in range(repetitions):
        if abs(summe_fehlerquadrate_ableitung(m-a, x, y)) < abs(summe_fehlerquadrate_ableitung(m, x, y)):
            m -= a
        else:    
            m += a
            a *= 0.5
            a = -a

    return m


x = list(i[0] for i in datensatz)
y = list(i[2] for i in datensatz)      

m = gradientenverfahren(x, y, 15)
print(summe_fehlerquadrate(m, x, y))
print(m)


y_p = [0, m * (max(x))]
x_p = [0, max(x)]
# print(x_p)
# print(y_p)
x_i = np.array(x)
y_i = np.array(y)
plt.plot(x_p, y_p)
plt.scatter(x_i, y_i)
plt.show()