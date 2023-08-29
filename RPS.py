import matplotlib.pyplot as plt
import numpy as np


# Parameters :

rA = 0.4
rB = 0.4
rC = 0.4

pA = 0.2
pB = 0.2
pC = 0.2

dA = 0.1
dB = 0.1
dC = 0.1

rhoAs = []
rhoBs = []
rhoCs = []
rhoVs = []
time = []

rhoA = 0.1
rhoB = 0.2
rhoC = 0.3
rhoV = 1 - (rhoA + rhoB + rhoC)
t = 0

dt = 0.01

for i in range(10000):
    rhoA = rhoA + dt * rhoA * (rA * rhoV - pC * rhoC - dA)
    rhoB = rhoB + dt * rhoB * (rB * rhoV - pA * rhoA - dB)
    rhoC = rhoC + dt * rhoC * (rC * rhoV - pB * rhoB - dC)
    t = t + dt

    rhoAs.append(rhoA)
    rhoBs.append(rhoB)
    rhoCs.append(rhoC)
    time.append(t)

plt.plot(time, rhoAs, label="A")
plt.plot(time, rhoBs, label="B")
plt.plot(time, rhoCs, label="C")
plt.legend()
plt.show()
