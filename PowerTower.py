from cProfile import label
import matplotlib.pyplot as plt
import numpy as np


#aax = []

#a = 1
#n = 20
#c = 1.44

c=np.linspace(1,1.4,10)

for j in c:
    aax = []
    a = 1
    n = 25
    for i in range(n):
        a = j ** a
        aax.append(a)

    plt.plot(aax, label=str(j))

plt.legend()
plt.show()