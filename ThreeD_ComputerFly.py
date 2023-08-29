import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from mpl_toolkits.mplot3d import Axes3D

def f(x,y,z,a,b):
    return math.sin(a*y)-z*math.cos(b*x)
def g(x,y,z,c,d):
    return z*math.sin(c*x)-math.cos(d*y)
def h(x,e):
    return e*math.sin(x)

file=open("ComputerFly.txt","w+")
x=0
y=0
z=0
t=0
calculatoion_step=10000
a=0.4
b=0.1
c=0.5
d=0.5
e=0.7
for i in range(calculatoion_step):
    x=f(x,y,z,a,b)
    y=g(x,y,z,c,d)
    z=h(x,e)
    t+=i*0.1
    csv.writer(file).writerow([t,x,y,z])
data=np.loadtxt("ComputerFly.txt",delimiter=',')
time=data[:,0]
x_pos=data[:,1]
y_pos=data[:,2]
z_pos=data[:,3]


fig=plt.figure()
ax=plt.axes(projection="3d")
ax.plot3D(x_pos,y_pos,z_pos)
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.set_title(' 3D Computer Fly')
plt.show()
