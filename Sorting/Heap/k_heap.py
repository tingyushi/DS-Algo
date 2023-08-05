import math

class K_Heap:

    data = []
    length = 0

    def __init__(self, values, k):
        self.data = values
        self.k = k
        self.length = len(values)
        self.build_heap(self.data)

    def build_heap(self, values):
        for i in range(self.length - 1, -1, -1):
            self.sink(i)

    def isIn(self, i):
        if (i >= 0 and i <= self.length - 1):
            return True
        return False

    def sink(self, i):
        if not (self.isIn(i)):
            return

        #remove non-children indicies
        children_list = self.children(i)
        temp = []
        for num in children_list:
            if (self.isIn(num)):
                temp.append(num)
        children_list = temp

        #no children exist
        if (len(children_list) == 0):
            return

        #find the maximum value of all the children
        current_max_index = children_list[0]
        for k in children_list:
            if (self.data[k] > self.data[current_max_index]):
                current_max_index = k

        #swap and recursion
        if (self.data[i] < self.data[current_max_index]):
            self.data[i], self.data[current_max_index] = self.data[current_max_index], self.data[i]
            self.sink(current_max_index)
    
    def swim(self, i):
        if (i == 0):
            return
        parent_index = self.parent(i)
        if (self.data[i] > self.data[parent_index]):
            self.data[i], self.data[parent_index] = self.data[parent_index], self.data[i]
            self.swim(parent_index)

    def get_max(self):
        if (self.length == 0):
            return
        return self.data[0]
    
    def extract_max(self):
        if (self.length == 0):
            return
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        ans = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return ans

    def insert(self, value):
        if (len(self.data) == self.length):
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.swim(self.length - 1)

    '''
    Return all the indices for the children of self.data[i].
    self.data[i] may not have children, need to check when use.
    '''
    def children(self, i):
        ans = []
        for k in range(self.k - 1, -1, -1):  
            ans.append(self.k * (i + 1) - k) 
        return ans

    def parent(self, i):
        return (i - 1) // self.k

