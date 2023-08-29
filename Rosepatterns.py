"""Code plots different patterns like flower petals using parametric forms."""

### Sahil Islam ###
### 06/06/2020 ###

import matplotlib.pyplot as plt
import numpy as np
import pygame


def rosePatterns(n, d):
    xs = []
    ys = []
    k = float(n / d)
    for theta in np.arange(0, 2 * np.pi * d, 0.001):
        r = np.cos(k * theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        xs.append(x)
        ys.append(y)


    return xs, ys


def plotLoop(n, d):
    xs, ys = rosePatterns(n, d)
    plt.plot(xs, ys)
    plt.grid()
    plt.show()


def dynamicVisual(n, d):
    pygame.init()
    display_width = 900
    display_height = 650

    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [200, 0, 0]

    def point(x, y):
        pygame.draw.circle(display_surface, red, (int(x), int(y)), 1, 1)

    display_surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("")

    xo = display_width / 2.
    yo = display_height / 2.
    scale = 200

    xs, ys = rosePatterns(n, d)

    game_exit = False
    while not game_exit:
        display_surface.fill(black)

        for i in range(len(xs)):
            point(scale * xs[i] + xo, scale * ys[i] + yo)
            pygame.display.update()
            clock.tick(500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


dynamicVisual(27, 11)
