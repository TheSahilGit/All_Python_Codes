### This code  draws 'Fractal Tree' using a recursive function.###
### Sahil Islam ###
### Date: 20/05/2020 ###

import pygame
import numpy as np
import math

pygame.init()

display_width = 900
display_height = 650

black = [0, 0, 0]
white = [255, 255, 255]
geeenv = [127, 255, 0]
red = [200, 0, 0]

display_surface = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fractal Tree")


def recursion_loop(x1, y1, l, theta, error):  # This is th recursive function. It does the main trick.
    if l > error:  # Termination condition.
        x2 = x1 + l * math.cos(theta * math.pi / 180.)
        y2 = y1 - l * math.sin(theta * math.pi / 180.)

        pygame.draw.line(display_surface, red, (int(x1), int(y1)), (int(x2), int(y2)), 2)

        recursion_loop(x2, y2, l * 0.85, theta + 20,
                       error)  # Calling the function inside it with slightly varied argument.
        recursion_loop(x2, y2, l * 0.85, theta - 20, error)
        pygame.display.update()
        clock.tick(100)



display_surface.fill(black)

# Initialization
l = 100
theta = 90
x1 = display_width / 2
y1 = display_height
#

recursion_loop(x1, y1, l, theta, 15)

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


