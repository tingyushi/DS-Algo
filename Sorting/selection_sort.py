from sorting_test import isCorrect


def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


if __name__ == '__main__':
    isCorrect(selection_sort)