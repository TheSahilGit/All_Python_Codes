############ INCOMPLETE  ###########
############ Inclusion of Snannon Entropy is not done yet. #########

import matplotlib.pyplot as plt
import numpy as np
import math
import csv

file = open("Lyapunov.txt", "w+")
n = 300
e = math.exp(1)

for r in np.arange(2.1, 3.9, 0.005):
    x = 0.5
    lamda = 0.0
    for i in range(n+1):
        x = r * x * (1 - x)
        lamda = lamda + math.log(abs(r - 2 * r * x))
        if i > 100:
            csv.writer(file).writerow([i, r, x, lamda/n])

data = np.loadtxt("Lyapunov.txt", delimiter=',')
rs = data[:, 1]
xs = data[:, 2]
lamda = data[:, 3]
plt.plot(rs, xs,'.')
plt.plot(rs, lamda,'.')

plt.show()

