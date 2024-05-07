import math

def m_multidimensional(multidimensional_floatlist):
    result = []
    for dimension in multidimensional_floatlist:
        result.append([m(dimension)])
    return np.array(result)    

def covariance(bifloatlist):
    return sum([x - m(bifloatlist[0]) for x in bifloatlist[0]][i] * [y - m(bifloatlist[1]) for y in bifloatlist[1]][i] for i in range(len([x - m(bifloatlist[0]) for x in bifloatlist[0]]))) / (len(bifloatlist[0]) - 1)

def s_multidimensional(multidimensional_floatlist):
    result = [[] for _ in multidimensional_floatlist]
    for y in range(len(multidimensional_floatlist)):
        for x in range(len(multidimensional_floatlist)):
            result[y].append(covariance([multidimensional_floatlist[y], multidimensional_floatlist[x]]))
    return np.array(result)

def gauss_multidimensional(x, m, s):
    return (1 / (math.sqrt(2 * math.pi * np.linalg.det(s)))) * math.e ** (-0.5 * (x - m).transpose() @ np.linalg.inv(s) @ (x-m))