import numpy as np


def partition(List, low, high):
    pivot = List[low]
    i = low + 1
    j = high - 1
    while True:

        while List[i] <= pivot and i < j:
            i += 1
        while List[j] > pivot and i < j:
            j -= 1

        if i <= j:
            List[i], List[j] = List[j], List[i]

        else:
            List[low], List[j] = List[j], List[low]
            return j


def QuickSort(List, low, high):
    if low < high - 1:
        j = partition(List, low, high)
        QuickSort(List, low, j)
        QuickSort(List, j + 1, high)

    return List


a = [ 1, 554, 454, 23, -69, 554, 102, 457, 6, 4, 2, 10]

b = QuickSort(a, 0, len(a))
print(b)
