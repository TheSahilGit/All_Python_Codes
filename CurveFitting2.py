import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import random
import csv

# Data File.

step = 50
x = np.zeros(step)
y = np.zeros(step)
for i in range(step):
    np.random.seed(100)
    x[i] = x[i - 1] + i * np.random.random()
    y[i] = i * np.random.random()

plt.scatter(x, y, marker='x',color='k')


def function(x, a, b, c, d, e, f):
    return a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f


a = 0.0000
b = 0.0000
c = 0.0000
d = 0.00005
e = -0.0005
f = 0
xdata = np.linspace(0, 600, step)
ydata = function(xdata, a, b, c, d, e, f)

p, q = curve_fit(function, xdata, ydata,bounds=(0.0,[0.001,0.001,0.001,0.05,0.5,0.0001]))
plt.plot(xdata, function(xdata, *p))

plt.show()
