import matplotlib.pyplot as plt
import numpy as np

N = 5000


def solveLoop(x, y):
    xs = []
    ys = []
    time = []

    t = 0.0
    dt = 0.001
    for i in range(N):
        x += dt * (3 - x - 2 * y)
        y += dt * (2 - x - y)
        t += dt

        xs.append(x)
        ys.append(y)
        time.append(t)

    return xs, ys


x = [0, 0, 3, 1, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 5]
y = [0, 2, 0, 1, 4, 0, 3, 2, 10, 9, 5, 1.5, 0, 2, 5, 6]

plotNo = len(x)
xsPlot = np.zeros((plotNo, N))
ysPlot = np.zeros((plotNo, N))

for i in range(len(xsPlot)):
    xsPlot[i, :], ysPlot[i, :] = solveLoop(x[i], y[i])

for i in range(len(xsPlot)):
    plt.plot(xsPlot[i, :], ysPlot[i, :], label="(x,y): " + str(x[i]) + "," + str(y[i]))

plt.legend()
plt.grid()
plt.show()
