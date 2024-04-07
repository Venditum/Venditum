import csv, matplotlib.pyplot as plt, math, multiprocessing, numpy as np, random, sys
from matplotlib import cm

def gauss(x, m, s):
    return (1/(s * math.sqrt(2 * math.pi)) * math.e) ** (-0.5 * ((x - m) / s) ** 2)

def m(liste):
    return sum(liste) / len(liste)

def s(liste):
    return math.sqrt((sum([(x - m(liste)) ** 2 for x in liste])) / len(liste))

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

def predict(testdatenzeile, arten_ms, gewichte):
    best = ""
    bestscore = 0

    for art in arten_ms: 
        totalscore = 0
        for i in range(len(testdatenzeile)):
            totalscore += gauss(testdatenzeile[i], arten_ms[art][i][0], arten_ms[art][i][1]) * gewichte[i]  
        if totalscore > bestscore:
            bestscore = totalscore
            best = art 
    return best

def validierung(durchläufe, gewichte, p):
    treffer = 0
    for _ in range(durchläufe):
        random.shuffle(datensatz)
        testdaten = datensatz[:int(len(datensatz) * p)]
        trainingsdaten = datensatz[int(len(datensatz) * p):]
        arten = {}

        for i in range(len(trainingsdaten)):
            if not trainingsdaten[i][-1] in arten:
                arten[trainingsdaten[i][-1]] = []       
            arten[trainingsdaten[i][-1]].append(trainingsdaten[i])
            
        arten_ms = {}

        for art in arten:
            arten_ms[art] = []
            for i in range(4):
                arten_ms[art].append((m(list(zip(*arten[art]))[i]), s(list(zip(*arten[art]))[i])))
    
        for zeile in testdaten:
            vermutung = predict(zeile[:-1], arten_ms, gewichte)
            if vermutung == zeile[-1]:
                treffer += 1

    return treffer / (len(testdaten) * durchläufe)

def gewichte_optimierung(gewichte_3_4):
    d_s = []
    for g_3, g_4 in gewichte_3_4:
        d = validierung(12, [1, 1, g_3, g_4], 0.2)
        d_s.append((d, g_3, g_4))
    return max(d_s), d_s

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

if __name__ == '__main__':
    anzahl_t = 8
    d = gewichte_optimierung_multithreaded([i / 4 for i in range(1, 200)], [i / 4 for i in range(1, 200)], anzahl_t)
    print(f"Beste Genauigkeit: {d[0][0]} bei g_3={d[0][1]} und g_4={d[0][2]}")
    fig = plt.figure("Genauigkeit")
    ax = fig.add_subplot(projection="3d")
    ax.plot_trisurf(np.array(list(zip(*d[1]))[1]), np.array(list(zip(*d[1]))[2]), np.array(list(zip(*d[1]))[0]), cmap=cm.coolwarm)
    ax.scatter(d[0][1], d[0][2], d[0][0], color="green", s=250)
    plt.xlabel("g_3")
    plt.ylabel("g_4")
    ax.legend(['Genauigkeit'])
    plt.show()