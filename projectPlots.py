import matplotlib.pyplot as plt
import numpy as np

H=np.linspace(-5,5,30)
T=np.linspace(1,6,6)
M=np.zeros((len(T),len(H)))

for t in range(len(T)):
    for h in range(len(H)):
        M[t,h]=np.tanh((3+H[h])/T[t])+ 6* np.tanh((1+H[h])*6/T[t])



for i in range(len(T)):
    plt.scatter(H, M[i:i+1], marker='.', label='T= '+ str(T[i]))


plt.xlabel("H")
plt.ylabel("M")
plt.legend()
plt.grid()
plt.show()



print(M)