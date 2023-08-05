import math


'''
This Heap uses pop when extracting max
'''
class Heap1:

    def __init__(self, L):
        self.data = L
        self.build_heap()        

    def __Swap__(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def get_length(self):
        return len(self.data)
    
    def build_heap(self):
        #bottom-up method
        i = self.get_length()
        while (i >= 0):
            self.heapify(i)
            i -= 1
    
    def isEmpty(self):
        if (self.get_length() == 0):
            return True
        return False

    ## @param i The index of parent
    #  @return The index of left child
    def left(self, i):
        return 2 * (i + 1) - 1

    ## @param i The index of parent
    #  @return The index of right child
    def right(self, i):
        return 2 * (i + 1)

    ## @details Find the parent of index i
    def parent(self, i):
        if (i % 2 == 1):
            parent_index = int(((i + 1) / 2) - 1)
        else:
            parent_index = int((i / 2) - 1)
        return parent_index

    ## @details This is the same as sink for 2C03; assume the structure below is a heap
    #  @param i The index number to be sinked
    def heapify(self, i):
        #find the max among parent, left child and rigth child
        max_index = i
        if (self.left(i) < self.get_length() and self.data[self.left(i)] > self.data[max_index]):
            max_index = self.left(i)
        if (self.right(i) < self.get_length() and self.data[self.right(i)] > self.data[max_index]):
            max_index = self.right(i)
        if (max_index != i):
            self.__Swap__(max_index, i)
            #recursive sink; the recursion should only happen when there is a swap;
            #otherwise stack overflaw
            self.heapify(max_index)
    
    ## @details This is the same as swim form 2C03
    #  @param i The index to be bubbled up
    def bubble_up(self, i):
        #base case definition
        # Empty list
        if (self.isEmpty()):
            return
        # root can not swim up
        if (i < 1):
            return

        parent_index = self.parent(i)
        if (self.data[i] > self.data[parent_index]):
            self.__Swap__(i, parent_index)
            self.bubble_up(parent_index)

    def insert_value(self, value):
        self.data.append(value)
        self.bubble_up(self.get_length() - 1)
    
    def extract_max(self):
        if (self.isEmpty()):
            return
        self.data[0], self.data[self.get_length() - 1] = self.data[self.get_length() - 1], self.data[0]
        ans = self.data.pop()
        self.heapify(0)
        return ans

    def __str__(self):
        height = math.ceil(math.log(self.get_length() + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.get_length())):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s


'''
This Heap does not use pop when extracting max
'''
import math

class Heap2:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s