import csv, math, random, matplotlib.pyplot as plt, multiprocessing, numpy as np, time
from matplotlib import cm


def abstand(zeile1, zeile2, gewichte):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] * gewichte[i] - zeile2[i] * gewichte[i]) ** 2
    return math.sqrt(n)

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])


datensatz_transponiert = list(zip(*datensatz))
maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 1):
        datensatz[i][j] /= maxima[j]

def krk(testdatenzeile, trainingsdaten, k, gewichte):
    abstände = []
    for zeile in trainingsdaten:
        abstände.append([abstand(zeile[:-1], testdatenzeile, gewichte), zeile[-1]])

    radius_k = list(filter(lambda x: x[0] <= k, abstände))

    if not radius_k:
        return ""

    vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)
    return vorhersage

def validierung(p: float, k: float, h: int, gewichte: list) -> float:
    treffer = 0
    
    for _ in range(h):
        random.shuffle(datensatz)
        testdaten = datensatz[:int(len(datensatz) * p)]
        trainingsdaten = datensatz[int(len(datensatz) * p):]

        for testdatenzeile in testdaten:
            vermutung = krk(testdatenzeile[:-1], trainingsdaten, k, gewichte)
            if vermutung == testdatenzeile[-1]:
                treffer += 1

    return treffer / (len(testdaten) * h)

def k_optimierung(n: int, gewichte: list):
    ergebnisse = []
    for k in range(n):
        erg = validierung(0.2, k / n, n // 2, gewichte)
        ergebnisse.append((erg, k / n))
    return max(ergebnisse, key=lambda x: x[0]), ergebnisse

def gewichte_optimierung(gewichte_3_4):
    d_s = []
    for g_3, g_4 in gewichte_3_4:
        d = k_optimierung(25, [1, 1, g_3, g_4])
        d_s.append([d[0][0], g_3, g_4])
    return max(d_s, key=lambda x:x[0]), d_s

def gewichte_optimierung_multithreaded(gewichte_3, gewichte_4, t):

    gewichte = [(i, j) for i in gewichte_3 for j in gewichte_4]
    trenn_indizes = [i for i in range(0, len(gewichte) + 1, len(gewichte) // t)]
    trenn_indizes[-1] = len(gewichte)
    gewichte_liste = [gewichte[trenn_indizes[i]:trenn_indizes[i + 1]] for i in range(t)]

    with multiprocessing.Pool(t) as pool:
        ergebnisse = pool.map(gewichte_optimierung, gewichte_liste)

    d_s = []
    for ergebnis in ergebnisse:
        d_s += ergebnis[1] 
    
    return max(ergebnisse)[0], d_s

x = time.time()

if __name__ == '__main__':
    anzahl_t = 8
    d = gewichte_optimierung_multithreaded([i / 4 for i in range(1, 10)], [i / 2 for i in range(1, 10)], anzahl_t)
    print(f"Beste Genauigkeit: {d[0][0]} bei g_3={d[0][1]} und g_4={d[0][2]}")
    print(time.time() - x)
    fig = plt.figure("Genauigkeit")
    ax = fig.add_subplot(projection="3d")
    ax.plot_trisurf(np.array(list(zip(*d[1]))[1]), np.array(list(zip(*d[1]))[2]), np.array(list(zip(*d[1]))[0]), cmap=cm.coolwarm)
    ax.scatter(d[0][1], d[0][2], d[0][0], color="green", s=250)
    plt.xlabel("g_3")
    plt.ylabel("g_4")
    ax.legend(['Genauigkeit'])
    plt.show()