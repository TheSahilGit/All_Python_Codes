

import matplotlib.pyplot as plt
import numpy as np



def fcos(i, theta):
    return (50 * 4 / ((2 * i + 1) * np.pi)) * np.cos((2 * i + 1) * theta * np.pi / 180.)


def fsin(i, theta):
    return (4 / ((2 * i + 1) * np.pi)) * np.sin((2 * i + 1) * theta * np.pi / 180.)


def mainLoop(frequency, max_n):
    w = frequency
    time = np.arange(150, 500, 0.1)
    y = []
    x = []
    n = max_n

    for t in range(len(time)):
        sumY = []
        sumX = []
        for i in range(n):
            sy = fsin(i, w * time[t])
            sx = fcos(i, w * time[t])
            sumY.append(sy)
            sumX.append(sx)

        y.append(sum(sumY))
        x.append(sum(sumX))

    plt.plot(time, y)
    plt.plot(x, y)
    plt.show()

mainLoop(10,10)