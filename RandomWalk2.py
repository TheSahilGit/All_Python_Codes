import matplotlib.pyplot as plt
import numpy as np


def randomWalk(totalStep, stepSize):
    x = 0
    y = 0
    xs = []
    ys = []
    rs = []
    step = []
    rms = []
    for i in range(totalStep):
        x += (np.random.random() - 0.5) * stepSize
        y += (np.random.random() - 0.5) * stepSize
        rsq = x * x + y * y
        r = np.sqrt(rsq)
        rmsr = float(r / np.sqrt(totalStep))

        xs.append(x)
        ys.append(y)
        rs.append(r)
        rms.append(rmsr)
        step.append(i)

    return xs, ys, rs, rms, step


xs, ys, rs, rms, step = randomWalk(10000, 1)
plt.plot(xs, ys)


plt.grid()
plt.show()
