import matplotlib.pyplot as plt
import numpy as np

xGrid = 20
yGrid = 20
positionX = np.linspace(0, xGrid, xGrid)
positionY = np.linspace(0, yGrid, yGrid)
u = np.zeros((xGrid, yGrid))

'''for x in range(xGrid):
    u[x, 0] = 0
    u[x, yGrid - 1] = 0
for y in range(yGrid):
    u[0, y] = 0
    u[xGrid - 1, y] = 0'''

for x in range(1, xGrid - 1):
    for y in range(1, yGrid - 1):
        u[x, y] = 100

'''plt.subplot(1, 2, 1)
plt.imshow(u)'''

itr = 0
while itr < 500:
    for x in range(xGrid - 1):
        for y in range(yGrid - 1):
            u[x, y] = (u[x + 1, y] + u[x, y + 1] + u[x - 1, y] + u[x, y - 1]) * 0.25
    itr += 1

'''plt.subplot(1, 2, 2)
plt.imshow(u)'''

ax = plt.axes(projection="3d")
ax.plot_wireframe(positionX, positionY, u)
plt.show()
