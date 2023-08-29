import matplotlib.pyplot as plt
import numpy as np
import csv
import random


def random_number(a, c, maxm, r, how_many):
    file = open("random_numbers.txt", "w+")
    for i in range(how_many):
        d = random.randint(0, maxm+1)
        csv.writer(file).writerow([r, r + 1, d, i])
        r = (a * r + c) % maxm

    file.close()


random_number(57, 1, 256, 10, 2000)
data = np.loadtxt("random_numbers.txt", delimiter=',')
r = data[:, 0]
r2 = data[:, 1]
d = data[:, 2]
i = data[:, 3]

plt.plot(i, d, 'o', label='Python Random Numbers')
plt.plot(i, r, 'o', label='My Random Numbers', color='orange')
plt.legend()
plt.show()


