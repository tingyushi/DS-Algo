'''
This file contain four different versions of mergesort
1. merge_self and merge_sort (in-place)
2. merge and mergesort (not in-place)
3. merge_three and mergesort_three (3-way mergesort)
4. merge_bottom and mergesort_bottom(bottom-up version, no dividing process)
'''
from sorting_test import isCorrect

def Swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def merge_bottom(L, start, mid, end):
    '''
    Tips:
    1. end is inclusive
    2. start is the beginning index of the first partition
    3. mid is the beginning index of the second partition
    4. end is the ending the second partition 
    '''
    temp = []
    i = start  # index for the first partition
    j = mid  # index for the second partition

    while (i < mid or j <= end):
        if (i == mid):
            while (j <= end):
                temp.append(L[j])
                j += 1
            break

        if (j == end + 1):
            while (i < mid):
                temp.append(L[i])
                i += 1
            break

        if (L[i] < L[j]):
            temp.append(L[i])
            i += 1
        else:
            temp.append(L[j])
            j += 1
    # assigning values back
    L_index = start
    temp_index = 0
    while (L_index <= end):
        L[L_index] = temp[temp_index]
        L_index += 1
        temp_index += 1

'''
mid = low + size
high = low + 2 * size - 1
'''
def mergesort_bottom(L):
    size = 1 #This is window size // 2
    length = len(L)
    last_index = length - 1
    while (size < length):
        low = 0
        #Make sure mid is always within the bound
        while (low < length - size):
            #Make sure high is within the bound
            if (low + 2 * size - 1 < last_index):
                merge_bottom(L, low, low + size, low + 2 * size - 1)
            else:
                merge_bottom(L, low, low + size, last_index)
            low += 2 * size
        size *= 2



def mergesort_three(L):
    if (len(L) <= 2):
        if (len(L) == 2 and L[1] < L[0]):
            Swap(L, 0, 1)
        return L

    distance = len(L) // 2
    left = L[:distance]
    mid = L[distance:2 * distance]
    right = L[2 * distance:]

    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)

    temp = merge_three(left, mid, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, mid, right):
    i = j = k = 0
    L = []
    # Handle one list first

    while (i < len(left) and j < len(mid) and k < len(right)):
        if (left[i] <= mid[j] and left[i] <= right[k]):
            L.append(left[i])
            i += 1
        elif (mid[j] <= left[i] and mid[j] <= right[k]):
            L.append(mid[j])
            j += 1
        else:
            L.append(right[k])
            k += 1

    if (i == len(left)):
        while (j < len(mid) or k < len(right)):
            if (j >= len(mid)):
                L.append(right[k])
                k += 1
            elif (k >= len(right)):
                L.append(mid[j])
                j += 1
            else:
                if (mid[j] <= right[k]):
                    L.append(mid[j])
                    j += 1
                else:
                    L.append(right[k])
                    k += 1
        return L
    elif (j == len(mid)):
        while (i < len(left) or k < len(right)):
            if (i >= len(left)):
                L.append(right[k])
                k += 1
            elif (k >= len(right)):
                L.append(left[i])
                i += 1
            else:
                if (left[i] <= right[k]):
                    L.append(left[i])
                    i += 1
                else:
                    L.append(right[k])
                    k += 1
        return L
    else:
        while (i < len(left) or j < len(mid)):
            if (i >= len(left)):
                L.append(mid[j])
                j += 1
            elif (j >= len(mid)):
                L.append(left[i])
                i += 1
            else:
                if (left[i] <= mid[j]):
                    L.append(left[i])
                    i += 1
                else:
                    L.append(mid[j])
                    j += 1
        return L



def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    # Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    # Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        # Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L


#We know that len(L1) + len(L2) == len(L) is true
def merge_self(L1, L2, L):
    i = 0 #pointer for L1
    j = 0 #pointer for L2
    k = 0 #pointer for L

    while (i < len(L1) or j < len(L2)):
        if (i == len(L1)):
            L[k] = L2[j]
            j += 1
            k += 1
        elif (j == len(L2)):
            L[k] = L1[i]
            i += 1
            k += 1
        elif (L1[i] < L2[j]):
            L[k] = L1[i]
            i += 1
            k += 1
        else:
            L[k] = L2[j]
            j += 1
            k += 1


#The following is the merge sort
def merge_sort(L):
    if (len(L) <= 1):
        return
    mid = len(L) // 2
    L1 = L[0:mid]
    L2 = L[mid:len(L)]

    merge_sort(L1)
    merge_sort(L2)

    merge_self(L1, L2, L)


if __name__ == '__main__':
    isCorrect(mergesort_bottom)
    isCorrect(mergesort_three)
    isCorrect(mergesort)
    isCorrect(merge_sort)