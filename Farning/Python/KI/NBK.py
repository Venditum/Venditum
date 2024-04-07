import csv, matplotlib.pyplot as plt, math, multiprocessing, numpy as np
from matplotlib import cm

def gauss(x, m, s):
    return (1/(s * math.sqrt(2 * math.pi)) * math.e) ** (-0.5 * ((x - m) / s) ** 2)

def m(liste):
    return sum(liste) / len(liste)

def s(datensatz):
    return math.sqrt((sum([(x - m(datensatz)) ** 2 for x in datensatz])) / len(datensatz))

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
        
arten_ms = {}

for art in arten:
    arten_ms[art] = []
    for i in range(4):
        arten_ms[art].append((m(list(zip(*arten[art]))[i]), s(list(zip(*arten[art]))[i])))

def predict(blume, gewichte):
    best = ""
    bestscore = 0
    for art in arten_ms: 
        totalscore = 0
        for i in range(len(blume)):
            totalscore += gauss(blume[i], arten_ms[art][i][0], arten_ms[art][i][1]) * gewichte[i]  
        if totalscore > bestscore:
            bestscore = totalscore
            best = art 
    return best

def validierung(gewichte):
    treffer = 0
    
    for i in range(len(datensatz)):
        vermutung = predict(datensatz[i][:-1], gewichte)
        if vermutung == datensatz[i][-1]:
            treffer += 1

    return treffer / len(datensatz)

def gewichte_optimierung(gewichte_3_4):
    d_s = []
    for g_3, g_4 in gewichte_3_4:
        d = validierung([1, 1, g_3, g_4])
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
    d = gewichte_optimierung_multithreaded([i / 100 for i in range(1100, 1400)], [i / 100 for i in range(800, 1100)], anzahl_t)
    print(f"Beste Genauigkeit: {d[0][0]} bei g_3={d[0][1]} und g_4={d[0][2]}")
    fig = plt.figure("Genauigkeit")
    ax = fig.add_subplot(projection="3d")
    ax.plot_trisurf(np.array(list(zip(*d[1]))[1]), np.array(list(zip(*d[1]))[2]), np.array(list(zip(*d[1]))[0]), cmap=cm.coolwarm)
    ax.scatter(d[0][1], d[0][2], d[0][0], color="green", s=250)
    plt.xlabel("g_3")
    plt.ylabel("g_4")
    ax.legend(['Genauigkeit'])
    plt.show()