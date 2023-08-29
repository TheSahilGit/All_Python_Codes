import numpy as np
import matplotlib.pyplot as plt
import pygame


def twoD_ArrayVisual(Array_dimension):
    def bubble_sort_2d(List):
        print("Unsorted: " + str(List))
        countx = 0
        county = 0
        for p in range(len(List)):
            for q in range(len(List) - 1):
                for r in range(len(List)):
                    if List[r, q] > List[r, q + 1]:
                        List[r, q], List[r, q + 1] = List[r, q + 1], List[r, q]
                        countx = countx + 1

        for j in range(len(List)):
            for k in range(len(List) - 1):
                for l in range(len(List)):
                    if List[k, l] > List[k + 1, l]:
                        List[k, l], List[k + 1, l] = List[k + 1, l], List[k, l]
                        county = county + 1

        print("Sorted: " + str(List) + "\nSwaps(Bubble Sort)= " + "(" + str(countx) + "," + str(county) + ")")
        return List

    # Defining Array :
    n = Array_dimension
    List = np.zeros([n, n])
    for a in range(n):
        for b in range(n):
            List[a, b] = np.random.randint(1, n)  # A (n x n)  array of integers from 1 to n.

    plt.subplot(2, 2, 1)
    plt.imshow(List)
    plt.title("Unsorted")

    bubble_sort_2d(List)

    plt.subplot(2, 2, 4)
    plt.imshow(List)
    plt.title("Sorted")

    plt.suptitle("Bubble Sort for 2D square array\n" + "Array dimension: " + str(n) + 'X' + str(n))
    plt.show()


def oneD_ArrayVisual(array_length):
    def bubbleSort(List):
        print("Unsorted: " + str(List))
        count = 0
        for i in range(len(List)):
            for j in range(len(List) - 1):
                if List[j] > List[j + 1]:
                    List[j], List[j + 1] = List[j + 1], List[j]
                    count = count + 1

        print("Sorted: " + str(List) + "\n No of swaps(Bubble Sort)= " + str(count))
        return List

    n = array_length
    a = np.zeros(n)
    x = np.zeros(len(a))
    for i in range(len(a)):
        x[i] = i
        a[i] = np.random.randint(1, n)

    plt.subplot(2, 2, 1)
    plt.plot(x, a)
    plt.title("Unsorted")

    bubbleSort(a)

    plt.subplot(2, 2, 4)
    plt.plot(x, a)
    plt.title("Sorted")

    plt.suptitle("Bubble Sort for 1D array\n" + "Array Length: " + str(n))
    plt.show()


def visual_loop():
    pygame.init()

    display_width = 900
    display_height = 650

    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [200, 0, 0]

    display_surface = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Bubble Sort")

    def rect(x, y, rectHeight, color):
        rectWidth = 10

        pygame.draw.rect(display_surface, color, [x, y, rectWidth, rectHeight])

    def sortLoop(list):
        for a in range(len(list)):
            for b in range(len(list) - 1):
                if list[b] > list[b + 1]:
                    list[b], list[b + 1] = list[b + 1], list[b]
        return list

    display_surface.fill(white)
    n = 100
    x = np.linspace(0, display_width, n, endpoint=False)
    rectHeight = np.zeros(n)

    for i in range(n):
        rectHeight[i] = np.random.randint(0, display_height)

    for i in range(len(x)):
        rect(x[i], display_height - rectHeight[i], rectHeight[i], black)

    for i in range(len(x)):
        sortLoop(rectHeight)

        rect(x[i], display_height - rectHeight[i], rectHeight[i], red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()


visual_loop()
