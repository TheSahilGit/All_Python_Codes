import matplotlib.pyplot as plt
import numpy as np


def f(l, x, y, z):
    nu1 = 2 * x * z
    nu2 = l * (l + 1) * y
    de = (1 - x * x)
    fr = (nu1 - nu2) / float(de)
    return fr


xs = []
ys = []
zs = []

l = 2
x = 0
y = 0
z = -0.5
h = 0.001
step = 1000
for i in range(step):
    z += h * f(l, x, y, z)
    y += h * z
    x += h

    xs.append(x)
    ys.append(y)
    zs.append(z)

print(xs)
print(ys)
plt.plot(xs, ys)

plt.show()
