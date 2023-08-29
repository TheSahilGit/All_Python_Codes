import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def f(a, b, x):
    #return a * np.sin(2*np.pi* b * x)
    return a*np.exp(-b*x*x)


n = 100
ao = 5
bo = 3
x = np.linspace(0, 1, n)
y = np.ones(n) * ao * f(ao, bo, x)
l, = plt.plot(x, y)

sliderAxes1 = plt.axes([0.12, 0.05, 0.8, 0.03])
sliderAxes2 = plt.axes([0.12, 0.01, 0.8, 0.03])

slider1 = Slider(sliderAxes1, 'a', 0.1, 30, valinit=ao, valstep=1)
slider2 = Slider(sliderAxes2, 'b', 0.1, 10, valinit=bo, valstep=0.1)


def update(value):
    a = slider1.val
    b = slider2.val
    l.set_ydata(np.ones(n) * f(a, b, x))


slider1.on_changed(update)
slider2.on_changed(update)

plt.show()
