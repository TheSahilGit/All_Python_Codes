import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import random


def V(x, y):
    return 0.5 * x * x + 0.5 * y * y + x * x * y - y * y * y / 3


def E(x, y, px, py):
    return 0.5 * px * px + 0.5 * py * py + V(x, y)


def f(x, y):
    return -x - 2 * x * y


def g(x, y):
    return -y - x * x + y * y


def calculation_loop(x, y, px, py):
    t = 0
    h = 0.01
    calculation_count = 1000
    file = open("HenonHelis.dat", "w+")
    for i in range(calculation_count):
        px = px + h * f(x, y)
        py = py + h * g(x, y)
        x = x + h * px
        y = y + h * py
        t = t + i * 0.1
        csv.writer(file).writerow([t, x, y, px, py])



def plot_loop1(x, y, px, py):
    e = E(x, y, px, py)
    calculation_loop(x, y, px, py)
    data = np.loadtxt("HenonHelis.dat", delimiter=',')
    time = data[:, 0]
    x_pos = data[:, 1]
    y_pos = data[:, 2]
    x_mom = data[:, 3]
    y_mom = data[:, 4]

    plt.subplot(4, 2, 1)
    plt.plot(time, x_pos)
    plt.grid()
    plt.title("x Position vs Time")
    plt.xlabel("Time")
    plt.ylabel("X Position")

    plt.subplot(4, 2, 2)
    plt.plot(time, y_pos)
    plt.grid()
    plt.title("y Position vs Time")
    plt.xlabel("Time")
    plt.ylabel("Y Position")

    plt.subplot(4, 2, 3)
    plt.plot(time, x_mom)
    plt.grid()
    plt.title("x Momentum vs Time")
    plt.xlabel("Time")
    plt.ylabel("X Momentum")

    plt.subplot(4, 2, 4)
    plt.plot(time, y_mom)
    plt.grid()
    plt.title("y Momentum vs Time")
    plt.xlabel("Time")
    plt.ylabel("Y Momentum")

    plt.subplot(4, 2, 5)
    plt.plot(x_pos, y_pos)
    plt.grid()
    plt.title("x Position Vs y Position ")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.subplot(4, 2, 6)
    plt.plot(x_mom, y_mom)
    plt.grid()
    plt.title("x Momentum Vs y Momentum ")
    plt.xlabel("X Momentum")
    plt.ylabel("Y Momentum")

    plt.subplot(4, 2, 7)
    plt.plot(x_pos, x_mom)
    plt.grid()
    plt.title("Phase Space in x")
    plt.xlabel("X Position")
    plt.ylabel("X Momentum")

    plt.subplot(4, 2, 8)
    plt.plot(y_pos, y_mom)
    plt.grid()
    plt.title("Phase Space in y")
    plt.xlabel("Y Position")
    plt.ylabel("Y Momentum")

    plt.suptitle("Henon Helis Potential Results\n" + "Initial Energy=" + str(round(e,5)))

    plt.subplots_adjust(0.12, 0.09, 0.90, 0.89, 0.29, 0.85)


def plot_loop2(x_start,x_end,y,px,py):
    for x in np.arange(x_init, x_end, 0.1):
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(time, x_pos, label="Initial Energy=" + str(round(e,5)))
        plt.title("Henon Helis Potential Results\n" + "Y Position Vs Time Graph for different initial condition ")
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("X Position")
    plt.grid()


def plot_loop3(x_start,x_end,y,px,py):
    for x in np.arange(x_start, x_end, 0.1):
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(time, y_pos, label="Initial Energy=" + str(round(e,5)))
        plt.title("Henon Helis Potential Results\n" + "Y Position Vs Time Graph for different initial condition ")
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("Y Position")
    plt.grid()


def plot_loop4(x_start,x_end,y,px,py):
    for x in np.arange(x_start, x_end, 0.1):
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(time, x_mom, label="Initial Energy=" + str(round(e,5)))
        plt.title("Henon Helis Potential Results\n" + "X Momentum Vs Time Graph for different initial condition ")
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("X Momentum")
    plt.grid()


def plot_loop5(x_start,x_end,y,px,py):
    for x in np.arange(x_start,x_end, 0.1):
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(time, y_mom, label="Initial Energy=" + str(round(e,5)))
        plt.title("Henon Helis Potential Results\n" + "Y Momentum Vs Time Graph for different initial condition ")
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("Y Momentum")
    plt.grid()


def plot_loop6(x_start,x_end,y,px,py):
    for x in np.arange(x_start,x_end, 0.1):
        y = 0.
        px = 0.1
        py = 0.
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(x_pos, x_mom, label="Initial Energy=" + str(round(e,5)))
        plt.title("Henon Helis Potential Results\n" + "Phase Space Trajectory in X for different initial condition ")
        plt.legend()
        plt.xlabel("X Position")
        plt.ylabel("X Momentum")
    plt.grid()


def plot_loop7(x_start,x_end,y,px,py):
    for x in np.arange(x_start,x_end, 0.07):
        e = E(x, y, px, py)
        calculation_loop(x, y, px, py)
        data = np.loadtxt("HenonHelis.dat", delimiter=',')
        time = data[:, 0]
        x_pos = data[:, 1]
        y_pos = data[:, 2]
        x_mom = data[:, 3]
        y_mom = data[:, 4]

        plt.plot(y_pos, y_mom, label="Initial Energy=" + str(round(e,5)))
        
        plt.title("Henon Helis Potential Results\n" + "Phase Space Trajectory in Y for different initial condition ")
        plt.legend()
        plt.xlabel("Y Position")
        plt.ylabel("Y Momentum")
    plt.grid()

plot_loop7(0.01,0.5,0.1,0,0)
plt.show()

