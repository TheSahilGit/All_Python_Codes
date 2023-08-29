import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import cauchy



'''x0=0.0
gamma=0.5
xs=[]
fs=[]

def f(x):
    return 1.0/(gamma*((1+(x-x0)/gamma))**2)


for x in range(-100,100):
    xs.append(x)
    fs.append(f(x))

plt.plot(xs,fs)
plt.show()'''

numargs = cauchy.numargs
[] = [0.6, ] * numargs
rv = cauchy()

print ("RV : \n", rv)
quantile = np.arange (0.01, 1, 0.1)
distribution = np.linspace(-5, np.minimum(rv.dist.b, 5))
print("Distribution : \n", distribution)
  
plot = plt.plot(distribution, rv.pdf(distribution))
plt.show()


