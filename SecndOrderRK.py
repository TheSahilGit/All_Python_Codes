import matplotlib.pyplot as plt
import numpy as np
import math
import csv


def f(w, x):
    return -w*w*x


def g(v):
    return v


def RK_plot_loop(w, x, v):
    h = 0.00001
    step = 100000
    t = 0
    fileone = open("SecondOrderRK.txt", "w+")
    for i in range(step):
        k1 = h * f(w, x)
        k2 = h * f(w, x + h / 2.)
        k3 = h * f(w, x + h/ 2.)
        k4 = h * f(w, h)

        m1 = h * g(v)
        m2 = h * g(v + h / 2.)
        m3 = h * g(v + h / 2.)
        m4 = h * g(v + h)

        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        x = x + (m1 + 2 * m2 + 2 * m3 + m4) / 6.0
        t =  i
        csv.writer(fileone).writerow([t, x, v])

    data = np.loadtxt("SecondOrderRK.txt", delimiter=',')
    time = data[:, 0]
    position = data[:, 1]
    velocity = data[:, 2]

    # plt.plot(time,velocity)
    plt.plot(time, position,label="RK")
    plt.legend()



def Euler_plot_loop(w, x, v):
    h = 0.00001
    step = 100000
    t = 0
    filetwo = open("SecondOrderEuler.txt", "w+")
    for i in range(step):
        x = x + h * g(v)
        v = v + h * f(w, x)
        t =  i
        csv.writer(filetwo).writerow([t, x, v])

    data = np.loadtxt("SecondOrderEuler.txt", delimiter=',')
    time = data[:, 0]
    position = data[:, 1]
    velocity = data[:, 2]

    # plt.plot(time, velocity)
    plt.plot(time, position,label="Euler")
    plt.legend()


w=10
x=0.0
v=0.5
Euler_plot_loop(w, x, v)
RK_plot_loop(w, x, v)
plt.title("SHM Solution by both RK4 and Euler Method\n"+"Initial Position= " +str(x)+ ", " + "Initial Velocity= " + str(v)+ ", " + "Frequecy= "+ str(w))
plt.grid()

plt.show()
