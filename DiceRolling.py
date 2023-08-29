"""Code simulates throwing dice using random number generator"""

### Sahil Islam ###
### 30/06/2020 ###


import numpy as np
import matplotlib.pyplot as plt

ones = []
twos = []
threes = []
fours = []
fives = []
sixes = []
xs = []

ratio12 = []
ratio23 = []
ratio34 = []
ratio45 = []
ratio56 = []
ratio61 = []

probability = 1 / 6.

o = 0
tw = 0
th = 0
fo = 0
fi = 0
s = 0
x = 0

maxThrow = 5000
for throw in range(100, maxThrow, 100):
    for i in range(throw):
        a = np.random.random()

        if 0 * probability < a < 1 * probability:
            o += 1

        if probability < a < 2 * probability:
            tw += 1

        if 2 * probability < a < 3 * probability:
            th += 1

        if 3 * probability < a < 4 * probability:
            fo += 1

        if 4 * probability < a < 5 * probability:
            fi += 1

        if 5 * probability < a < 6 * probability:
            s += 1

    ones.append(o)
    twos.append(tw)
    threes.append(th)
    fours.append(fo)
    fives.append(fi)
    sixes.append(s)

    xs.append(throw)
    ratio12.append(o / tw)
    ratio23.append(tw / th)
    ratio34.append(th / fo)
    ratio45.append(fo / fi)
    ratio56.append(fi / s)
    ratio61.append(s / o)


def ratioPlot():
    plt.subplot(2, 3, 1)
    plt.plot(xs, ratio12)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of ones and twos")
    plt.grid()

    plt.subplot(2, 3, 2)
    plt.plot(xs, ratio23)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of twos and threes")
    plt.grid()

    plt.subplot(2, 3, 3)
    plt.plot(xs, ratio34)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of threes and fours")
    plt.grid()

    plt.subplot(2, 3, 4)
    plt.plot(xs, ratio45)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of fours and fives")
    plt.grid()

    plt.subplot(2, 3, 5)
    plt.plot(xs, ratio56)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of fives and sixes")
    plt.grid()

    plt.subplot(2, 3, 6)
    plt.plot(xs, ratio61)
    plt.xlabel("No of total throws")
    plt.ylabel("Ratio of sixes and ones")
    plt.grid()

    plt.suptitle(" Dice Throw \n Ratio of different outcomes for different no of total throws")
    plt.subplots_adjust(0.09, 0.11, 0.95, 0.90, 0.42, 0.33)
    plt.show()



ratioPlot()