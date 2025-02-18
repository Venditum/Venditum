import csv, matplotlib.pyplot as plt, numpy as np
from mpl_toolkits import mplot3d

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

def summe_fehlerquadrate(steigung, x_real, y_real):
    return sum((steigung * x_real[i] - y_real[i]) ** 2 for i in range(len(x_real)))

def summe_fehlerquadrate_ableitung(steigung, x_real, y_real):
    return sum(2 * (steigung*x_real[i] - y_real[i]) * x_real[i] for i in range(len(x_real)))

def summe_fehlerquadrate_mehrdimensional_ableitung(w, x, y):
    return 2*((np.matrix.transpose(x) @ x))@ w - 2*(np.matrix.transpose(x)) @ y

def gradientenverfahren(x, y, repetitions):
    m = y[-1] / x[-1]
    a = 0.00001
    for i in range(repetitions):
        m -= a * summe_fehlerquadrate_ableitung(m, x, y)
    return m

def gradientenverfahren_mehrdimensional(x, y, repetitions):
    m = np.array([[x[0][0]], [x[0][1]]])
    a = 0.0001
    for i in range(repetitions):
        m = m - a * summe_fehlerquadrate_mehrdimensional_ableitung(m, x, y)
    print(summe_fehlerquadrate_mehrdimensional_ableitung(m, x, y))
    return m    


for art in datensatz_nach_art:
    x_matrix = np.array([i[:-2] for i in datensatz_nach_art[art]])
    y_matrix = np.array([[i[-2]] for i in datensatz_nach_art[art]])
    x_1 = [i[0] for i in x_matrix]
    x_2 = [i[1] for i in x_matrix]
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x_1, x_2, y_matrix)
    ax.plot3D([0, max(x_1)],[0, max(x_2)],[0, (x_matrix[5] @ gradientenverfahren_mehrdimensional(x_matrix, y_matrix, 1000))[0]])
plt.show()