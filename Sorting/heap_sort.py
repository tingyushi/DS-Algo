from sorting_test import isCorrect
from Heap.heap import Heap2
from Heap.k_heap import K_Heap

def heap_sort(L):
    h = Heap2(L)
    temp = []
    for _ in range(len(L)):
        temp.insert(0, h.extract_max())

    for idx, value in enumerate(temp):
        L[idx] = value

def k_heap_sort(L):
    K = 5
    kh = K_Heap(L, K)

    temp = []
    for _ in range(len(L)):
        temp.insert(0, kh.extract_max())

    for idx, value in enumerate(temp):
        L[idx] = value


if __name__ == '__main__':
    isCorrect(heap_sort)
    isCorrect(k_heap_sort)
    