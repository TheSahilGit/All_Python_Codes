'''Visulising Fourier Series and square wave generator using pygame. '''

### Sahil Islam ###
### 01/06/2020 ###

import pygame
import numpy as np
import math

pygame.init()

display_width = 850
display_height = 540

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Fourier")
clock = pygame.time.Clock()


def point(x, y, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), 1)


def circle(x, y, r):
    pygame.draw.circle(screen, white, (int(x), int(y)), int(r), 1)


def fcos(i, theta):
    return (70 * 4 / ((2 * i + 1) * math.pi)) * np.cos((2 * i + 1) * theta * math.pi / 180.)


def fsin(i, theta):
    return (70 * 4 / ((2 * i + 1) * math.pi)) * np.sin((2 * i + 1) * theta * math.pi / 180.)


def calculationLoop(frequency, max_n):
    xo = display_width / 8.
    yo = display_height / 2.
    w = frequency

    y = []
    x = []
    n = max_n

    time = np.arange(display_width / 2. + 100, display_width-50, 0.1)

    for t in range(len(time)):
        sumY = []
        sumX = []
        for i in range(n):
            sy = fsin(i, w * time[t])
            sx = fcos(i, w * time[t])
            sumY.append(sy)
            sumX.append(sx)

        y.append(sum(sumY) + yo)
        x.append(sum(sumX) + xo)
    return time, x, y



frequency=10
maximumN=10

display_exit = False
while not display_exit:
    screen.fill(black)
    time, x, y = calculationLoop(frequency,maximumN)

    for i in range(len(time)):
        point(x[i] + 100, y[i], green)
        point(time[i], y[i], red)
        pygame.display.update()
        clock.tick(70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_exit = True
                pygame.quit()
                quit()
