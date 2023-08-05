from sorting_test import isCorrect

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


def bubble_sort_opt1(L):
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


def bubble_sort_opt2(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swaps += 1
        if swaps == 0:
            return


def bubble_sort_opt3(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swaps += 1
        if swaps == 0:
            return


if __name__ == '__main__':
    isCorrect(bubble_sort)
    isCorrect(bubble_sort_opt1)
    isCorrect(bubble_sort_opt2)
    isCorrect(bubble_sort_opt3)