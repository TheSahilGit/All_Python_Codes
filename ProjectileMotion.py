import pygame
import matplotlib.pyplot as plt
import numpy as np

pygame.init()
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


def ball(x, y):
    pygame.draw.circle(screen, red, (int(x), int(y)), 5)


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(("Score: " + str(count)), True, white)
    screen.blit(text, (0, 0))


def netForce(m, g, c, v):
    f = m * g - c * v * v
    return f


clock = pygame.time.Clock()

xPos = 0
yPos = height

'''tantheta = 0
if pygame.mouse.get_pressed()[0]:
    mouseX, mouseY = pygame.mouse.get_pos()

    tantheta = float((yPos - mouseY) / (mouseX - xPos))

theta = np.arctan(tantheta)'''

mass = 10
c = 0.000
u = 100
theta = 70
rad = np.pi / 180.
xVel = u * np.cos(theta * rad)
yVel = -u * np.sin(theta * rad)
g = 9.8
yAcc = float(netForce(mass, g, c, yVel)) / mass
xAcc = float(netForce(mass, 0, c, yVel)) / mass

count = 0
h = 0.1

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    ball(xPos, yPos)
    '''pygame.draw.line(screen, white, (xPos, yPos),
                     (xPos + xPos * np.tan(theta * rad), yPos - yPos * np.tan(theta * rad)))'''
    score(count)

    xVel += h * xAcc
    yVel += h * yAcc
    xPos += h * xVel
    yPos += h * yVel

    if yPos >= height:
        yVel *= -1
        count += 1
    if xPos >= width or xPos <= 0:
        xVel *= -1
        count += 1

    pygame.display.update()
    clock.tick(100)
