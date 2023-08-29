import matplotlib.pyplot as plt
import numpy as np
import random
import math
import csv
from numpy.random import rand

def decay_loop():
    file = open("decay.txt", "w+")
    t = 0
    n = 500
    n1 = 500
    h = 0.01
    for i in range(1000):
        lam = random.random()
        n = n - lam  #Not sure about this code
        t = i
        n1 = n1 - h * lam * n1


        csv.writer(file).writerow([n,n1, t])

    file.close()


def plot_loop():
    data = np.loadtxt("decay.txt", delimiter=',')
    n = data[:, 0]
    n1 = data[:, 1]
    t=data[:,2]
    plt.semilogy(t, n, label='Discrete Decay')
    plt.semilogy(t, n1, label='Continuas Decay')
    plt.legend()
    plt.xlabel("t")
    plt.ylabel("Number of Particles")


for i in range(11):
    print(rand())
