import matplotlib.pyplot as plt
import numpy as np
import math
import csv

file = open("sawtooth1.txt", "w+")


def first_loop(time_period):
    t = 0
    y = 0

    for t in np.arange(t, time_period + time_period / 8, time_period / 8):

        if 0 <= t <= time_period / 2:
            y = t / (time_period / 2)
        if time_period / 2 <= t <= time_period:
            y = (t - time_period) / (time_period / 2)

        csv.writer(file).writerow([t, y])

    file.close()


def plot_loop():
    data = np.loadtxt("sawtooth1.txt", delimiter=',')
    time = data[:, 0]
    position = data[:, 1]

    plt.plot(time, position)
    plt.grid()


for T in np.arange(2 * math.pi, 8 * math.pi, 2 * math.pi):
    first_loop(T)
plot_loop()
plt.show()
