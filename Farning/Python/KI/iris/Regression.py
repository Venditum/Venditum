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

def regressionsgerade(eingabe, x, y):
    m = sum([i * j for i in x for j in y]) / sum([i**2 for i in x]) / len(x)
    return m*eingabe

def regressionsgerademultidimensional(eingabe, x, y):    
    w = (np.linalg.inv(np.matrix.transpose(x) @ x)) @ np.matrix.transpose(x) @ np.matrix.transpose(y)
    #print(x)
    # print(x.shape())
    # print(eingabe.shape())
    # print(w.shape())
    print(w)
    return np.matrix.transpose(eingabe) @ w
    

y = [0, regressionsgerade(max([i[0] for i in datensatz]), [i[0] for i in datensatz], [i[2] for i in datensatz])]
x = [0, max([i[0] for i in datensatz])]
x_i = np.array([i[0] for i in datensatz])
y_i = np.array([i[2] for i in datensatz])
plt.plot(x, y)
plt.scatter(x_i, y_i)
plt.show()

for art in datensatz_nach_art:
    xyz = [0, regressionsgerademultidimensional(np.array(max([(sum(i[:-1]), (i[:-1])) for i in datensatz_nach_art[art]])[1]), np.array([i[:-1] for i in datensatz_nach_art[art]]), np.array([i[-1] for i in datensatz_nach_art[art]]))]
    print(xyz)
    print(np.array([i[:-2] for i in datensatz_nach_art[art]]))

    print(regressionsgerademultidimensional(np.array([5.4]), np.array([i[:-3] for i in datensatz_nach_art[art]]), np.array([i[-3] for i in datensatz_nach_art[art]])))

w_matrix = np.array([[1],[2]])

for art in datensatz_nach_art:
    x_matrix = np.array([i[:-2] for i in datensatz_nach_art[art]])
    y_matrix = np.array([i[-2] for i in datensatz_nach_art[art]])
    x_1 = [i[0] for i in x_matrix]
    x_2 = [i[1] for i in x_matrix]
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x_1, x_2, y_matrix)
    ax.plot3D([0, max(x_1)],[0, max(x_2)],[0, regressionsgerademultidimensional(x_matrix[5], x_matrix, y_matrix)])
plt.show()