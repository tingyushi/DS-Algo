'''
This file contains four different methods of building a heap
'''
import math

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap4()

    
    def build_heap1(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)
    
    def build_heap2(self):
        if (len(self.data) == 0):
            return
        temp = Heap([])
        for i in range(len(self.data)):
            temp.insert(self.data[i])
        for i in range(len(temp.data)):
            self.data[i] = temp.data[i]
    
    def is_heap(self):
        result = True
        for i in range(self.length - 1, 0, -1):
            if (self.data[self.parent(i)] < self.data[i]):
                result = False
                break
        return result
    
    def build_heap3(self):
        while not (self.is_heap()):
            for i in range(self.length):
                self.sink(i)

    def build_heap4(self):
        loop_time = math.floor(math.log(self.length, 2))
        for _ in range(loop_time):
            for i in range(self.length):
                self.sink(i)
        
    def sink(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

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
        self.sink(0)
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
