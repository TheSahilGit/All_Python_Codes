import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def derivative(t,y,r,w):
    u1,u2= np.split(y,2)
    du1dt = u2 #r * u1 - w * u2 - (u1**2 + u2**2) * u1
    du2dt = -u1 #r * u2 + w * u1 - (u1**2 + u2**2) * u2

    return np.concatenate([du1dt,du2dt])

r, w = 1, 1
Nr = 1
tmax, Nt = 100, 50
times = np.linspace(0, tmax, Nt)

# Initial condition
u10, u20 = 2*np.random.rand(Nr)-1, 2*np.random.rand(Nr)-1
y0 = 2 * np.concatenate([u10,u20])

# Solve
sol = solve_ivp(derivative, t_span=[0,tmax], y0=y0, t_eval=times, args=(r, w), method='BDF')

# Parse solution

u1, u2 =np.split(sol.y, 2, axis=0)





fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6), dpi=100, sharex=True)
ax1.set_ylabel(r'$u_1$')
ax2.set_ylabel(r'$u_2$')
ax2.set_xlabel(r'$t$')
for i in range(min(5, Nr)):
    ax1.plot(times, u1[i], lw=1)
    ax2.plot(times, u2[i], lw=1)

fig, ax = plt.subplots(1, figsize=(8,6), dpi=100)
ax.set_aspect(1)
for i in range(Nr):
    uplt, = ax.plot(u1[i], u2[i], lw=1)
    ax.plot(u1[i,0], u2[i,0], 'o', ms=2, color=uplt.get_color())
ax.set_xlabel(r'$u_1$')
ax.set_ylabel(r'$u_2$');

plt.show()


