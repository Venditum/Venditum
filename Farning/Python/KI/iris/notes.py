import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
z =[]
for i in x:
    for j in y:
        z.append(func(np.array([i, j]), np.array([1, 1]), np.array([0, 0])))
z = np.array(z).reshape(len(x), len(y))
plt.contourf(x, y, z)
plt.show()