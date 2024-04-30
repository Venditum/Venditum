import math

def m(floatlist):
    return sum(floatlist) / len(floatlist)

def s(floatlist):
    return math.sqrt((sum([(x - m(floatlist)) ** 2 for x in floatlist])) / (len(floatlist) - 1))

def m_multidimensional(multidimensional_floatlist):
    result = []
    for dimension in multidimensional_floatlist:
        result.append([m(dimension)])
    return result    

def covariance(bifloatlist):
    return sum([x - m(bifloatlist[0]) for x in bifloatlist[0]][i] * [y - m(bifloatlist[1]) for y in bifloatlist[1]][i] for i in range(len([x - m(bifloatlist[0]) for x in bifloatlist[0]]))) / (len(bifloatlist[0]) - 1)

def s_multidimensional(multidimensional_floatlist):
    result = [[] for _ in multidimensional_floatlist]
    for y in range(len(multidimensional_floatlist)):
        for x in range(len(multidimensional_floatlist)):
            result[y].append(covariance([multidimensional_floatlist[y], multidimensional_floatlist[x]]))
    return result