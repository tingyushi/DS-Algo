from sorting_test import isCorrect
from insertion_sort import insertion_sort2

def Swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp 



def quicksort_inplace_rec(L, left, right):
    #base case condition
    if (left >= right):
        return
    pivot_value = L[right]
    i = left
    j = right - 1
    while (i <= j):
        #find the first element bigger that pivot point on the left side
        while(i <= j and L[i] < pivot_value):
            i += 1
        #find the first element smaller that pivot point on the right side
        while (i <= j and L[j] > pivot_value):
            j -= 1
        #Swaping and moving pointers
        if (i <= j):
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
    L[i], L[right] = L[right], L[i]
    #quick sort left partition
    quicksort_inplace_rec(L, left, i - 1)
    #quick sort right partition
    quicksort_inplace_rec(L, i + 1, right)



def quicksort_inplace(L):
    quicksort_inplace_rec(L, 0, len(L) - 1)



def dual_copy(L):
    if len(L) < 2:
        return L
    
    #Choose L[0] as p1 and L[len(L) - 1] as p2, the following code
    # make sure that p1 < p2
    if (L[0] > L[len(L) - 1]):
        Swap(L, 0, len(L) - 1) 

    p1 = L[0] #left pivot
    p2 = L[len(L) - 1] #right pivot

    left = []
    middle = []
    right = []

    for num in L[1: len(L) - 1]:
        if (num < p1):
            left.append(num)
        elif (num < p2):
            middle.append(num)
        else:
            right.append(num)
    return dual_copy(left) + [p1] + dual_copy(middle) + [p2] + dual_copy(right)



def dual_pivot_quicksort(L):
    copy = dual_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]



def tri_copy(L):
    if (len(L) <= 2):
        if (len(L) == 2 and L[0] > L[1]):
            Swap(L, 0, 1)
        return L
    
    '''
    Rules for choosing three pivots
    p1 = L[0]
    p2 = L[1]
    p3 = L[2]
    Make sure p1 < p2 < p3
    ''' 
    if (L[0] > L[1]):
        Swap(L, 0, 1)
    if (L[0] > L[2]):
        Swap(L, 0, 2)
    if (L[1] > L[2]):
        Swap(L, 1, 2)

    #three pivot points
    p1 = L[0]
    p2 = L[1]
    p3 = L[2]

    #four partitions
    part1 = []
    part2 = []
    part3 = []
    part4 = []

    for num in L[3:]:
        if (num < p1):
            part1.append(num)
        elif (num < p2):
            part2.append(num)
        elif (num < p3):
            part3.append(num)
        else:
            part4.append(num)
    return tri_copy(part1) + [p1] + tri_copy(part2) + [p2] + tri_copy(part3) + [p3] + tri_copy(part4)



def tri_pivot_quicksort(L):
    copy = tri_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]



def quad_copy(L):
    #base case
    if (len(L) <= 3):
        if (len(L) == 2 and L[0] > L[1]):
            Swap(L, 0, 1)
        if (len(L) == 3):
            if (L[0] > L[1]):
                Swap(L, 0, 1)
            if (L[0] > L[2]):
                Swap(L, 0, 2)
            if (L[1] > L[2]):
                Swap(L, 1, 2)
        return L
    
    pivot_list = []
    
    #Choose pivot points
    for i in range(4):
        pivot_list.append(L[i])
    pivot_list.sort()
    p1 = pivot_list[0]
    p2 = pivot_list[1]
    p3 = pivot_list[2]
    p4 = pivot_list[3]
    
    #creating partitions
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    part5 = []

    for num in L[4:]:
        if (num < p1):
            part1.append(num)
        elif (num < p2):
            part2.append(num)
        elif (num < p3):
            part3.append(num)
        elif (num < p4):
            part4.append(num)
        else:
            part5.append(num)
    
    #recursive call 
    return quad_copy(part1) + [p1] + quad_copy(part2) + [p2] + quad_copy(part3) + [p3] + quad_copy(part4) + [p4] + quad_copy(part5)


def quad_pivot_quicksort(L):
    copy = quad_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


#if the list size is less than 7, insertion sort will be used since it is faster for shorter list
def quick_sort_opt_copy(L):
    if (len(L) <= 7):
        insertion_sort2(L)
        return L
    
    '''
    Rules for choosing three pivots
    p1 = L[0]
    p2 = L[1]
    p3 = L[2]
    Make sure p1 < p2 < p3
    ''' 
    if (L[0] > L[1]):
        Swap(L, 0, 1)
    if (L[0] > L[2]):
        Swap(L, 0, 2)
    if (L[1] > L[2]):
        Swap(L, 1, 2)

    #three pivot points
    p1 = L[0]
    p2 = L[1]
    p3 = L[2]

    #four partitions
    part1 = []
    part2 = []
    part3 = []
    part4 = []

    for num in L[3:]:
        if (num < p1):
            part1.append(num)
        elif (num < p2):
            part2.append(num)
        elif (num < p3):
            part3.append(num)
        else:
            part4.append(num)
    return tri_copy(part1) + [p1] + tri_copy(part2) + [p2] + tri_copy(part3) + [p3] + tri_copy(part4)



def quick_sort_opt(L):
    copy = quick_sort_opt_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


if __name__ == '__main__':
    isCorrect(quicksort_inplace)
    isCorrect(dual_pivot_quicksort)
    isCorrect(tri_pivot_quicksort)
    isCorrect(quad_pivot_quicksort)
    isCorrect(quick_sort_opt)