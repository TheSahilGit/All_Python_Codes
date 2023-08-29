import matplotlib.pyplot as plt
import numpy as np
import math
from tabulate import tabulate
import pygame


def f1(m1, m2, theta):
    g = 9.8
    return (m2 * g * np.sin(theta * math.pi / 180.) * np.cos(theta * math.pi / 180.)) / (
            m2 + m1 * np.sin(theta * math.pi / 180.) * np.sin(theta * math.pi / 180))


def f2(m1, m2, theta):
    g = 9.8
    return (m1 * g * np.sin(theta * math.pi / 180) * np.cos(theta * math.pi / 180)) / (
            m2 + m1 * np.sin(theta * math.pi / 180) * np.sin(theta * math.pi / 180))


def main_loop(m1, m2, theta, t_init, x1_init, x2_init, v1_init, v2_init):
    step = 1000
    h = 0.001

    # Array Defining for plotting:
    x1_pos = np.zeros(step)
    x1_vel = np.zeros(step)
    x2_pos = np.zeros(step)
    x2_vel = np.zeros(step)
    time = np.zeros(step)

    c = np.zeros(step)

    # Euler Implementation:
    def Euler_loop():
        t = t_init
        x1 = x1_init
        x2 = x2_init
        v1 = v1_init
        v2 = v2_init
        for i in range(step):
            v1 = v1 + h * f1(m1, m2, theta)
            x1 = x1 + h * v1

            v2 = v2 + h * f2(m1, m2, theta)
            x2 = x2 + h * v2

            t = t + h * i

            x1_pos[i] = x1
            x2_pos[i] = x2
            x1_vel[i] = v1
            x2_vel[i] = v2
            time[i] = t
            c[i] = m1 * v1 - m2 * v2

    def plot_loop1():
        Euler_loop()
        # Plotting
        plt.subplot(2, 2, 1)
        plt.plot(time, x1_pos,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", $theta$= " + str(
                     round(theta)))
        plt.xlabel("time")
        plt.ylabel("Displacement of Plane($x_1$)")
        plt.title("Horizontal displacement of Inclined Plane")
        plt.legend(loc='lower right', prop={"size": 8})

        plt.subplot(2, 2, 2)
        plt.plot(time, x1_vel,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)))
        plt.xlabel("time")
        plt.ylabel("Velocity of Plane($v_1$)")
        plt.title("Horizontal velocity of Plane")
        plt.legend(loc='lower right', prop={'size': 9})

        plt.subplot(2, 2, 3)
        plt.plot(time, x2_pos,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)))
        plt.xlabel("time")
        plt.ylabel("Displacement of Box($x_2$)")
        plt.title("Horizontal displacement of Box")
        plt.legend(loc='lower right', prop={'size': 9})

        plt.subplot(2, 2, 4)
        plt.plot(time, x2_vel,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)))
        plt.xlabel("time")
        plt.ylabel("Velocity of Box($v_2$)")
        plt.title("Horizontal velocity of Box")
        plt.legend(loc='lower right', prop={'size': 9})

        plt.suptitle(
            "Box on an Inclined Moving Plane Problem\n" + "Initial position and velocity of Plane and Box:\n" + "$x_{plane}$= " + str(
                x1_init) + ", " + "$v_{plane}$= " + str(v1_init) + ", " + "$x_{box}$= " + str(
                x2_init) + ", " + "$v_{box}$= " + str(
                v2_init) + "\n Horizontal Acceleration of the plane ($a_x$) =" + str(round(f1(m1, m2, theta), 3)))

        plt.subplots_adjust(0.12, 0.10, 0.92, 0.81, 0.36, 0.52)

    def plot_loop2():
        Euler_loop()
        # Plotting
        plt.subplot(2, 2, 1)
        plt.plot(time, x1_pos,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", $theta$= " + str(
                     round(theta)) + ", $a_{x,plane}$=" + str(round(f1(m1, m2, theta), 3)))
        plt.xlabel("time")
        plt.ylabel("Displacement of Plane($x_1$)")
        plt.title("Horizontal displacement of Inclined Plane")
        plt.legend(loc='upper left', prop={"size": 7})

        plt.subplot(2, 2, 2)
        plt.plot(time, x1_vel,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)) + ", $a_{x,plane}$=" + str(round(f1(m1, m2, theta), 3)))
        plt.xlabel("time")
        plt.ylabel("Velocity of Plane($v_1$)")
        plt.title("Horizontal velocity of Plane")
        plt.legend(loc='upper left', prop={'size': 6})

        plt.subplot(2, 2, 3)
        plt.plot(time, x2_pos,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)) + ", $a_{x,plane}$=" + str(round(f1(m1, m2, theta), 3)))
        plt.xlabel("time")
        plt.ylabel("Displacement of Box($x_2$)")
        plt.title("Horizontal displacement of Box")
        plt.legend(loc='upper left', prop={'size': 8})

        plt.subplot(2, 2, 4)
        plt.plot(time, x2_vel,
                 label="$m_1$= " + str(m1) + ", $m_2$= " + str(m2) + ", theta= " + str(
                     round(theta)) + ", $a_{x,plane}$=" + str(round(f1(m1, m2, theta), 3)))
        plt.xlabel("time")
        plt.ylabel("Velocity of Box($v_2$)")
        plt.title("Horizontal velocity of Box")
        plt.legend(loc='upper left', prop={'size': 6})

        plt.suptitle(
            "Box on an Inclined Moving Plane Problem\n" + "Initial position and velocity of Plane and Box:\n" + "$x_{"
                                                                                                                "plane}$= " + str(
                x1_init) + ", " + "$v_{plane}$= " + str(v1_init) + ", " + "$x_{box}$= " + str(
                x2_init) + ", " + "$v_{box}$= " + str(
                v2_init))

        plt.subplots_adjust(0.12, 0.10, 0.92, 0.81, 0.36, 0.52)

    def table_loop():
        Euler_loop()
        heads = ["x1_init", "x2_init", "v1_init", "v2_init", "m1", "m2", "theta", "Acceleration of the Plane",
                 "Horizontal Acceleration of the Box"]
        data = [(str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta),
                 str(f1(m1, m2, theta)), str(f2(m1, m2, theta))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1 + 10), str(m2), str(theta),
                 str(f1(m1 + 10, m2, theta)), str(f2(m1 + 10, m2, theta))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1 + 20), str(m2), str(theta),
                 str(f1(m1 + 20, m2, theta)), str(f2(m1 + 20, m2, theta))),
                ("----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----"),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta),
                 str(f1(m1, m2, theta)), str(f2(m1, m2, theta))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2 + 10), str(theta),
                 str(f1(m1, m2 + 10, theta)), str(f2(m1, m2 + 10, theta))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2 + 20), str(theta),
                 str(f1(m1, m2 + 20, theta)), str(f2(m1, m2 + 20, theta))),
                ("----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----"),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta),
                 str(f1(m1, m2, theta)), str(f2(m1, m2, theta))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta - 15),
                 str(f1(m1, m2, theta - 15)), str(f2(m1, m2, theta - 15))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta + 15),
                 str(f1(m1, m2, theta + 15)), str(f2(m1, m2, theta + 15))),
                ("----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----"),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1 + 20), str(m2), str(theta - 15),
                 str(f1(m1 + 20, m2, theta - 15)), str(f2(m1 + 20, m2, theta - 15))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1 + 20), str(m2), str(theta - 35),
                 str(f1(m1 + 20, m2, theta - 35)), str(f2(m1 + 20, m2, theta - 35))),

                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1 + 20), str(m2), str(theta - 40),
                 str(f1(m1 + 20, m2, theta - 40)), str(f2(m1 + 20, m2, theta - 40))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta + 35),
                 str(f1(m1 + 20, m2, theta + 35)), str(f2(m1 + 20, m2, theta + 35))),
                ("----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----"),

                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta - 45),
                 str(f1(m1, m2, theta - 45)), str(f2(m1, m2, theta - 45))),
                (str(x1_init), str(x2_init), str(v1_init), str(v2_init), str(m1), str(m2), str(theta + 40),
                 str(f1(m1, m2, theta + 40)), str(f2(m1, m2, theta + 40))),
                ]

        print(tabulate(data, headers=heads))

    def plot_loop3():
        Euler_loop()
        plt.plot(time, c, label="$x_{plane}$= " + str(x1_init) + ", " + "$v_{plane}$= " + str(
            v1_init) + ", " + "$x_{box}$= " + str(x2_init) + ", " + "$v_{box}$= " + str(v2_init))
        plt.title("Box on an Inclined Moving Plane Problem\n" + "$m_1=$" + str(m1) + " and " + "$m_2$=" + str(m2))
        plt.xlabel("time")
        plt.ylabel("$m_1 v_1 - m_2 v_2$")
        plt.legend()

    plot_loop2()


def gameLoop():
    step = 1000
    h = 0.001

    # Array Defining for plotting:
    x1_pos = np.zeros(step)
    x1_vel = np.zeros(step)
    x2_pos = np.zeros(step)
    x2_vel = np.zeros(step)
    time = np.zeros(step)

    def Euler_loop(m1, m2, theta, t_init, x1_init, x2_init, v1_init, v2_init):
        t = t_init
        x1 = x1_init
        x2 = x2_init
        v1 = v1_init
        v2 = v2_init
        for i in range(step):
            v1 = v1 + h * f1(m1, m2, theta)
            x1 = x1 + h * v1

            v2 = v2 + h * f2(m1, m2, theta)
            x2 = x2 + h * v2

            t = t + h * i

            x1_pos[i] = x1
            x2_pos[i] = x2
            x1_vel[i] = v1
            x2_vel[i] = v2
            time[i] = t

    theta = 45
    l = 200
    x1_init=1
    x2_init=1

    Euler_loop(100, 10, theta, 0, x1_init, x2_init, 0, 0, )

    def plane(x1, y1):
        x2 = x1 + l * np.cos(theta * math.pi / 180.)
        y2 = y1 + l * np.sin(theta * math.pi / 180.)
        pygame.draw.line(display_surface, black, [x1, y1], [x2, y2])

    def box(x, y):
        pygame.draw.rect(display_surface, red, [x, y, 25., 25])

    pygame.init()
    display_width = 900
    display_height = 650

    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [200, 0, 0]
    purple = [138, 43, 226]
    whiten = [230, 230, 250]
    green = [0, 255, 0]
    blue = [0, 0, 255]

    display_surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("")

    game_exit = False
    while not game_exit:
        display_surface.fill(whiten)
        for i in range(len(x1_pos)):
            x_plane = -x1_pos[i] * 100
            y_plane = (x1_init + x2_init)* np.tan(theta * math.pi / 180.) * 100
            x_box = x2_pos[i] * 100
            y_box = (x1_pos[i] + x2_pos[i]) * np.tan(theta * math.pi / 180.) * 100


            plane(x_plane, y_plane)
            box(x_box, y_box)

            pygame.display.update()
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    pygame.quit()
    quit()


gameLoop()
