'''
Red Black Tree
'''

class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        # can not rotate leaf
        if self.is_leaf():
            return

        if self.parent == None:
            is_root = True
        else:
            is_root = False

        temp = self

        if temp.left == None:
            return

        if is_root:
            left_kid = temp.left
            left_kid_right_kid = left_kid.right
            left_kid.right = temp
            temp.parent = left_kid
            temp.left = left_kid_right_kid
            if left_kid_right_kid != None:
                left_kid_right_kid.parent = temp
            left_kid.parent = None
        else:
            if self.is_left_child():
                is_left_kid = True
            else:
                is_left_kid = False
            temp_parent = temp.parent
            left_kid = temp.left
            left_kid_right_kid = left_kid.right
            left_kid.right = temp
            temp.parent = left_kid
            temp.left = left_kid_right_kid
            if left_kid_right_kid != None:
                left_kid_right_kid.parent = temp
            if is_left_kid:
                temp_parent.left = left_kid
            else:
                temp_parent.right = left_kid
            left_kid.parent = temp_parent


    def rotate_left(self):
        #can not rotate leaf
        if self.is_leaf():
            return

        #check if self is root
        if self.parent == None:
            is_root = True
        else:
            is_root = False

        temp = self #temp points self

        #if temp has no left child -> return
        if temp.right == None:
            return

        if is_root:
            right_kid = temp.right
            right_kid_left_kid = right_kid.left
            right_kid.left = temp
            temp.parent = right_kid
            temp.right = right_kid_left_kid
            if right_kid_left_kid != None:
                right_kid_left_kid.parent = temp
            right_kid.parent = None
        else:
            if self.is_left_child():
                is_left_child = True
            else:
                is_left_child = False
            temp_parent = temp.parent 
            right_kid = temp.right 
            right_kid_left_kid = right_kid.left 
            right_kid.left = temp
            temp.parent = right_kid
            temp.right = right_kid_left_kid
            if right_kid_left_kid != None:
                right_kid_left_kid.parent = temp
            if is_left_child:
                temp_parent.left = right_kid
            else:
                temp_parent.right = right_kid
            right_kid.parent = temp_parent



class RBTree:

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
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)
    
    '''
    CASES:
    1. P is red and U is red
    2. P is red and U is black
    2.1 P(left)G and N(left)P
    2.2 P(left)G and N(right)P
    2.3 P(right)G and N(right)P
    2.4 P(right)G and N(left)P
    after 2.2, 2.1 is needed
    after 2.4, 2.3 is needed
    '''

    def fix(self, node):
        if node.parent == None:
            node.make_black()
            return
        
        while node != None and node.parent != None and node.parent.is_red(): 
            if (node.parent).is_left_child(): #node's parent is the left child
                uncle = node.get_uncle()
                #make sure uncle is not None
                if (uncle != None) and uncle.is_red():
                    (node.parent).make_black()
                    uncle.make_black()
                    (node.parent.parent).make_red()
                    node = node.parent.parent
                else:
                    if node.is_right_child(): #node is the right child  -> case 2.2
                        node = node.parent
                        node.rotate_left()
                    # node is the left child, this is also needed after the above case -> case 2.1
                    if node.parent.parent == self.root:
                        flag1 = True
                    else:
                        flag1 = False
                    (node.parent).make_black()
                    (node.parent.parent).make_red()
                    (node.parent.parent).rotate_right()
                    if flag1:
                        self.root = node.parent
            else:  #node's parent is the right child
                uncle = node.get_uncle()
                #make sure uncle is not None
                if (uncle != None) and uncle.is_red(): #case 1
                    (node.parent).make_black()
                    uncle.make_black()
                    (node.parent.parent).make_red()
                    node = node.parent.parent
                else:
                    if node.is_left_child(): #node is left child -> case 2.4
                        node = node.parent #after right rotation, make sure node points to lower object
                        node.rotate_right()
                    # node is right child case 2.3, this is needed after above case
                    if node.parent.parent == self.root:
                        flag2 = True
                    else:
                        flag2 = False
                    (node.parent).make_black()
                    (node.parent.parent).make_red()
                    (node.parent.parent).rotate_left()
                    if flag2:
                        self.root = node.parent
        self.root.make_black()
        

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
