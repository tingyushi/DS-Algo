from sorting_test import isCorrect

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


# traditional implementation
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# improved version
# instead of swap all the time, find where to insert directly
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)



def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value  # if the value to be inserted is the smallest one.

if __name__ == '__main__':
    isCorrect(insertion_sort)
    isCorrect(insertion_sort2)