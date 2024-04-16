import csv, matplotlib.pyplot as plt, math, multiprocessing, numpy as np, random, sys
from matplotlib import cm

def gauss(x, m, s):
    return (1/(s * math.sqrt(2 * math.pi)) * math.e) ** (-0.5 * ((x - m) / s) ** 2)

def poisson(x, l):
    return (math.e ** (-l) * l ** x) / math.factorial(int(x))   

def m(floatlist):
    return sum(floatlist) / len(floatlist)

def s(floatlist):
    return math.sqrt((sum([(x - m(floatlist)) ** 2 for x in floatlist])) / len(floatlist))

dataset = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        dataset.append([float(value) for value in line[:-1]] + [line[-1]])

speciesdic = {}

for line in dataset:
    if not line[-1] in speciesdic:
        speciesdic[line[-1]] = []       
    speciesdic[line[-1]].append(line[:-1])
    
dataset_species_ms = {}

for species in speciesdic:
    dataset_species_ms[species] = []
    for i in range(4):
        dataset_species_ms[species].append((m(list(zip(*speciesdic[species]))[i]), s(list(zip(*speciesdic[species]))[i])))

for species in dataset_species_ms:
    for i in range(len(dataset)):
        if dataset[i][-1] == species:
            for j in range(len(dataset[i]) - 1):
                dataset[i][j] = (dataset[i][j] - dataset_species_ms[species][j][0]) / dataset_species_ms[species][j][1]  

print(dataset)                                                     

def predict(testdataline, trainingsdata_species_ms, importance):
    best = ""
    bestscore = 0

    for species in trainingsdata_species_ms: 
        totalscore = 1
        for i in range(len(testdataline)):
            totalscore *= gauss(testdataline[i], trainingsdata_species_ms[species][i][0], trainingsdata_species_ms[species][i][1]) * importance[i]
            #totalscore += gauss(testdataline[i], trainingsdata_species_ms[species][i][0], trainingsdata_species_ms[species][i][1]) * importance[i]
            #totalscore *= gauss(testdataline[i], trainingsdata_species_ms[species][i][0], trainingsdata_species_ms[species][i][1])
        if totalscore > bestscore:
            bestscore = totalscore
            best = species
    return best

def evaluate(repetitions, importance, p):
    right = 0
    for _ in range(repetitions):
        random.shuffle(dataset)
        testdata = dataset[:int(len(dataset) * p)]
        trainingsdata = dataset[int(len(dataset) * p):]
        speciesdic = {}

        for line in trainingsdata:
            if not line[-1] in speciesdic:
                speciesdic[line[-1]] = []       
            speciesdic[line[-1]].append(line[:-1])
            
        trainingsdata_species_ms = {}

        for species in speciesdic:
            trainingsdata_species_ms[species] = []
            for i in range(4):
                trainingsdata_species_ms[species].append((m(list(zip(*speciesdic[species]))[i]), s(list(zip(*speciesdic[species]))[i])))
    
        for line in testdata:
            guess = predict(line[:-1], trainingsdata_species_ms, importance)
            if guess == line[-1]:
                right += 1

    return right / (len(testdata) * repetitions)

def importance_optimisation(importance_3_4):
    results = []
    for i_3, i_4 in importance_3_4:
        result = evaluate(12, [1, 1, i_3, i_4], 0.2)
        results.append((result, i_3, i_4))
    return max(results), results

def importance_optimisation_multithreaded(importance_3, importance_4, t):

    importance = [(i, j) for i in importance_3 for j in importance_4]
    split_indices = [i for i in range(0, len(importance) + 1, len(importance) // t)]
    split_indices[-1] = len(importance)
    importance_list = [importance[split_indices[i]:split_indices[i + 1]] for i in range(t)]

    with multiprocessing.Pool(t) as pool:
        results = pool.map(importance_optimisation, importance_list)
    
    totalresults = []
    for result in results:
        totalresults += result[1]

    return max(results)[0], totalresults

# if __name__ == '__main__':
#     number_t = 8
#     d = importance_optimisation_multithreaded([i / 2 for i in range(1, 100)], [i / 2 for i in range(1, 100)], number_t)
#     print(f"Best accuracy: {d[0][0]} at i_3={d[0][1]} and i_4={d[0][2]}")
#     fig = plt.figure("accuracy")
#     ax = fig.add_subplot(projection="3d")
#     ax.plot_trisurf(np.array(list(zip(*d[1]))[1]), np.array(list(zip(*d[1]))[2]), np.array(list(zip(*d[1]))[0]), cmap=cm.coolwarm)
#     ax.scatter(d[0][1], d[0][2], d[0][0], color="green", s=250)
#     plt.xlabel("i_3")
#     plt.ylabel("i_4")
#     ax.legend(['accuracy'])
#     plt.show()

print(evaluate(1, [1, 1, 1, 1], 0.2))