import matplotlib.pyplot as plt
import numpy as np
import pygame


def oneD(List_Length):
    def sort_loop(List):
        print("Unsorted: " + str(List))
        count = 0
        for i in range(len(List)):
            for j in range(i, len(List)):
                if List[i] > List[j]:
                    List[i], List[j] = List[j], List[i]
                    count = count + 1

        print("Sorted:" + str(List) + "\n No of swaps(Selection Sort)= " + str(count))
        return List

    n = List_Length
    a = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        a[i] = np.random.randint(1, n)
        x[i] = i

    plt.subplot(2, 2, 1)
    plt.plot(x, a)
    plt.title("Unsorted")



    sort_loop(a)


    plt.subplot(2, 2, 4)
    plt.plot(x, a)
    plt.title("Sorted")

    plt.suptitle("Selection Sort ")
    plt.show()


def twoD(Aray_Length):
    def sortLoop(Array):
        print("Unsorted: " + str(Array))
        countx=0
        county=0
        for i in range(len(Array)):
            for j in range(len(Array)):
                for k in range(len(Array)):
                    if Array[i, j] > Array[i, k]:
                        Array[i, j], Array[i, k] = Array[i, k], Array[i, j]
                        countx=countx+1
        for a in range(len(Array)):
            for b in range(len(Array)):
                for c in range(len(Array)):
                    if Array[c, a] > Array[b, a]:
                        Array[c, a], Array[b, a] = Array[b, a], Array[c, a]
                        county=county+1

        print("Sorted: " + str(Array)+ "\nSwaps(Selection)= " + "(" + str(countx) + "," + str(county) + ")")

    n = Aray_Length
    a = np.zeros([n, n])
    for e in range(n):
        for f in range(n):
            a[e, f] = np.random.randint(1, n)

    plt.subplot(2, 2, 1)
    plt.imshow(a)
    plt.title("Unsorted")

    sortLoop(a)

    plt.subplot(2, 2, 4)
    plt.imshow(a)
    plt.title("Sorted")

    plt.suptitle("Selection Sort 2D")
    plt.show()


def visual_loop():
    pygame.init()

    display_width = 900
    display_height = 650

    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [200, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 200]

    display_surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Selection Sort")

    def rect(x, y, rectHeight, color):
        rectWidth = 25

        pygame.draw.rect(display_surface, color, [x, y, rectWidth, rectHeight])

    n = 100
    x = np.linspace(0, display_width, n, endpoint=False)
    rectHeight = np.zeros(n)

    for i in range(n):
        rectHeight[i] = np.random.randint(0, display_height)

    color = black

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_surface.fill(white)

        for i in range(len(x)):
            rect(x[i], display_height - rectHeight[i], rectHeight[i], black)

        for i in range(len(x)):
            rect(x[i], display_height - rectHeight[i], rectHeight[i], color)
            for a in range(len(rectHeight)):
                for b in range(a, len(rectHeight)):

                    if rectHeight[a] > rectHeight[b]:
                        rectHeight[a], rectHeight[b] = rectHeight[b], rectHeight[a]

            rect(x[i], display_height - rectHeight[i], rectHeight[i], red)

            if rectHeight[i + 1] < rectHeight[i]:
                game_exit = True
            else:
                pygame.display.update()
                clock.tick(5)

    pygame.quit()
    quit()



#oneD(10)
visual_loop()

