import matplotlib.pyplot as plt
import numpy as np
import pygame

G = 100005


def force(m1, m2, r):
    if r > 0:
        f = - G * m1 * m2 / float(r * r)
    if r < 0:
        f = G * m1 * m2 / float(r * r)
    return f


pygame.init()

width = 1200
height = 900
screen = pygame.display.set_mode((width, height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()


def ball(x, y, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), 10, 5)


mBody = 10
mAttractor = 1000
r = 50
vBody = 5
vAttractor = 0
aBody = 0
aAttractor = 0

xo = width / 2.
yo = height / 2.

dt = 0.01

while True:
    screen.fill(white)

    r += dt * vBody
    vBody += dt * aBody
    aBody = dt * force(mBody, mAttractor, r) / float(mBody)

    x = r * np.cos(np.pi / 4.)
    y = r * np.cos(np.pi / 4.)
    ball(x + xo, y + yo, black)
    ball(width / 2., height / 2., red)
    pygame.display.update()
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
