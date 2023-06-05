'''
Binary search tree
This binary search tree does not allow duplicated values
'''

class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def __str__(self):
        #return f"Value: {self.value} -- Address: {id(self)}"
        return str(self.value)


class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):

        # handle the case that the value has already existed
        if node.value == value:
            return
        if value < node.value:
            if node.left == None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)

    # if the value is found, return the node
    def search(self, targetValue):
        # handle the empty tree case
        if self.is_empty():
            return None
        
        if (self.root.value == targetValue):
            return self.root
        else:
            return self.__search(self.root, targetValue)

    def __search(self, node, targetValue):

        if node.value == targetValue:
            return node
        
        # if node has no children and the value is not found, return none
        if node.left == None and node.right == None:
            return None
        
        if targetValue < node.value:
            return self.__search(node.left, targetValue)
        else:
            return self.__search(node.right, targetValue)


    def delete(self, targetValue):
        searchResult = self.search(targetValue)

        if searchResult == None:
            return
        
        # if the node is a leaf node
        if searchResult.is_leaf():
            if searchResult.parent == None:  # the tree only has the root node and we need to delete it
                print("=== FLAG ===")
                self.root == None
            elif searchResult.is_left_child():
                searchResult.parent.left = None
            else:
                searchResult.parent.right = None
            del searchResult
            return

        # if the node has only left child
        if ((searchResult.left != None) and (searchResult.right == None)):
            kid = searchResult.left 
            if searchResult.parent == None:
                self.root = kid ; kid.parent = None
            else:
                parent = searchResult.parent
                if searchResult.is_left_child():
                    parent.left = kid
                else:
                    parent.right = kid
                kid.parent = parent
            del searchResult
            return
        
        # if the node has only right child
        if ((searchResult.left == None) and (searchResult.right != None)):
            kid = searchResult.right
            if searchResult.parent == None:
                self.root = kid ; kid.parent = None
            else:
                parent = searchResult.parent
                if searchResult.is_left_child():
                    parent.left = kid
                else:
                    parent.right = kid
                kid.parent = parent
            del searchResult
            return
        
        # if the node has two children
        minNode = self.__findMinValue(searchResult.right)
        searchResult.value = minNode.value
        if minNode.is_left_child():
            minNode.parent.left = None
        else:
            minNode.parent.right = None
        minNode.parent = None
        del minNode
        return

    # find the minimum value in a tree
    def __findMinValue(self, root):
        node = root
        while node.left != None:
            node = node.left
        return node
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
