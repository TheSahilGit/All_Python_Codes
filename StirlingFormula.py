import matplotlib.pyplot as plt
import math


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def StirlingApprox(n):
    return n * math.log(n) - n


x = []
y1 = []
y2 = []
y3 = []

for i in range(1, 600):
    x.append(i)
    a = math.log(fact(i))
    b = StirlingApprox(i)
    y1.append(a)
    y2.append(b)
    y3.append(abs(a-b))


def loop1():
    plt.plot(x, y1, label="Log Fact")
    plt.plot(x, y2, label="Approx")

    plt.grid()
    plt.legend()
    plt.show()


def loop2():
    plt.plot(x, y3)
    plt.grid()
    plt.show()


loop2()
