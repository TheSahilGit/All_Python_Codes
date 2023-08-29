import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 500)


def f(r, x):
    return r * x * (1 - x)


def g(x):
    return x


r = 3.9
y1s = []
y2s = []

for i in x:
    y1 = f(r, i)
    y2 = g(i)

    y1s.append(y1)
    y2s.append(y2)

px = np.empty(100)
py = np.empty(100)
xo = 0.1
px[0] = xo
py[0] = 0
px[1] = xo
py[1] = f(r, px[0])
for j in range(1, len(px) - 1):
    px[j + 1] = py[j]
    py[j + 1] = f(r, px[j])

plt.plot(x, y1s)
plt.plot(x, y2s)
plt.plot(px, py)
plt.plot()
plt.grid()
plt.show()
