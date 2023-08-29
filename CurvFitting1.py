import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.optimize import curve_fit
import math


# Definition what kind of fit we want.
def f(x, a, b, c):

    return a*x**5+b*x**4+c



# Data to fit:
a = 2.5
b = 1.3
c = 0.5

xdata = np.linspace(-5, 5, 50)
y = f(xdata, a, b, c)

np.random.seed(1700)
y_noise = 0.2*np.random.normal(size=xdata.size)
ydata = y + y_noise

plt.scatter(xdata, ydata, label='data', color='black', marker='x')

# Now the part where we fit the data:
# We will use the same function to fit with parameters a,b,c adjusted.

popt, pcov = curve_fit(f, xdata, ydata)
plt.plot(xdata, f(xdata, *popt), label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

# popt2, pcov2 = curve_fit(f, xdata, ydata, bounds=(0.2, [2., 1.5, 1.0]))
# plt.plot(xdata, f(xdata, *popt2), label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt2))

plt.xlabel("x")
plt.ylabel("y")
plt.title("Data and Fit data Plot")
plt.legend()
plt.show()
