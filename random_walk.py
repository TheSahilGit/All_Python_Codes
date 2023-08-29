import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import math
import matplotlib.animation as animation
from matplotlib import style


def distance(number_of_steps, step_size):
    x = 0
    y = 0
    r = math.sqrt(x * x + y * y)
    rms = math.sqrt(r * r / math.sqrt(number_of_steps))
    file = open("random_walk1.txt", "w+")
    for i in range(number_of_steps + 1):
        csv.writer(file).writerow([x, y, r, i, math.sqrt(i), rms])
        x += (random.random() - 0.5) * step_size
        y += (random.random() - 0.5) * step_size
        r = math.sqrt((x * x + y * y))
        rms = math.sqrt(r * r) / math.sqrt(number_of_steps)

    file.close()


def draw(n):
    data = np.loadtxt("random_walk1.txt", delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    r = data[:, 2]
    i = data[:, 3]
    root_i = data[:, 4]
    rms = data[:, 5]

    plt.subplot(2, 1, 1)
    plt.plot(x, y, label="Walk No: " + str(n + 1))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    plt.title("Position curve")

    plt.subplot(2, 1, 2)
    plt.plot(i, r, label="Walk No: " + str(n + 1))
    plt.xlabel("Time")
    plt.ylabel("Distance")
    plt.legend()

    plt.title("Distance from the origin curve")


def plot_number(n):
    for i in range(n):
        distance(1000, 2)
        draw(n)
        plt.grid()


plot_number(2)
plt.show()
quit()
