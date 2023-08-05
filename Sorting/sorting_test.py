import random
import math

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1, 100 * n))
    return L

def isCorrect(sorting_func):
    L1 = create_random_list(500) ; L2 = L1.copy()
    sorting_func(L1) ; L2.sort()

    if (len(L1) != len(L2)):
        print("Sorting Function is incorrect") ; return
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            print("Sorting Function is incorrect") ; return
    print("Sorting Function is correct") ; return
