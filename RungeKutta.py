import matplotlib.pyplot as plt
import numpy as np
import math
import csv


def f(uo):
    return uo


def e(uy, t):
    g = 9.8
    return uy - g * t

def projectile_plot(u,theta_deg):
    h = 0.0001
    step = 100000
    y = 0
    x = 0
    t = 0
    pi=math.acos(-1.)
    theta_rad=theta_deg*pi/180.
    ux = u * math.cos(theta_rad)
    uy = u * math.sin(theta_rad)
    file = open("RungeKutta_Projectile.txt", "w+")
    for i in range(step):
        k1 = h * f(ux)
        k2 = h * f(ux)
        k3 = h * f(ux)
        k4 = h * f(ux)

        m1 = h * e(uy, t)
        m2 = h * e(uy, t + h / 2.0)
        m3 = h * e(uy, t + h / 2.0)
        m4 = h * e(uy, t + h)

        x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6.
        y = y + (m1 + 2 * m2 + 2 * m3 + m4) / 6.
        t = h * i
        if y>0:
            csv.writer(file).writerow([t, x, y])

    data = np.loadtxt("RungeKutta_Projectile.txt", delimiter=',')
    time = data[:, 0]
    x_pos = data[:, 1]
    y_pos = data[:, 2]

    plt.plot(x_pos, y_pos,label="Initial Velocity, Angle="+ str(u) + "," + str(theta_deg))
    plt.title("Projectile Motion")
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.legend()
    plt.grid()


projectile_plot(10,45)
projectile_plot(20,45)
projectile_plot(30,45)
projectile_plot(40,45)
projectile_plot(50,45)
plt.show()
