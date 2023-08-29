#########################################################
### EQUILIBRIUM ANALYSIS OF PARTICLES IN THREE BOXES ####
################# INCOMPLETE ############################


import matplotlib.pyplot as plt
import numpy as np
import math
import random

step = 10000
N = 1200
n_left = N
n_middle = 0
n_right = 0
t = 0

particle_left = np.zeros(step)
particle_middle = np.zeros(step)
particle_right = np.zeros(step)
time = np.zeros(step)

for i in range(step):
    particle_left[i] = n_left
    particle_middle[i] = n_middle
    particle_right[i] = n_right
    time[i] = t

    prob1 = n_left / N
    prob2 = n_middle / N
    x = random.random()
    y = random.random()

    if prob1 > x:
        n_left = n_left - 1
        n_middle = n_middle + 1
        if prob2 > y:
            n_middle = n_middle - 1
            n_right = n_right + 1

    if prob1 > x:
        n_left = n_left - 1
        n_middle = n_middle + 1

        if prob2 <= y:
            n_middle = n_middle + 1
            n_right = n_right - 1

    if prob1 <= x:
        n_left = n_left + 1
        n_middle = n_middle - 1
        if prob2 > y:
            n_middle = n_middle - 1
            n_right = n_right + 1

    if prob1 <= x:
        n_left = n_left + 1
        n_middle = n_middle - 1

        if prob2 <= y:
            n_middle = n_middle + 1
            n_right = n_right - 1

    '''if prob1 > x and prob2 > y:
        n_left = n_left - 1
        n_middle = n_middle - 1
        n_right = n_right + 1 + 1

    if prob1 <= x and prob2 <= y:
        n_left = n_left + 1 + 1
        n_middle = n_middle - 1
        n_right = n_right - 1

    if prob1 > x and prob2 <= y:
        n_left = n_left - 1
        n_middle = n_middle + 1 + 1
        n_right = n_right - 1

    if prob1 <= x and prob2 > y:
        n_left = n_left + 1
        n_middle = n_middle - 1 - 1
        n_right = n_right + 1'''

    t = t + 1

plt.plot(time, particle_middle, label="middle")
plt.plot(time, particle_left, label="left")
plt.plot(time, particle_right, label="right")
plt.legend()
plt.grid()
plt.show()
