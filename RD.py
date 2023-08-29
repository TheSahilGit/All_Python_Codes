# Finite difference Method.
# A PDE gets converted into set of ODE-s. 
#  When applied to PDE we get a set of coupled non-linear ODE-s.

# Diffusion Equation



import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def derivative(t,y,r):
    return r*y*y**3


r = -1
tmax,Nt = 10,100
times = np.linspace(0, tmax, Nt)

y0 = [np.random.rand(), ]


# look up--> Toplets matrix 


#sol = solve_ivp(derivative, t_span =[0 tmax], y0=y0, t_eval=times. args=(r,))
y = sol.y

