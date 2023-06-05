'''
This is the testing file for binary search tree
'''
import random
import math
from bst import BST


#no repiteded values
def create_random_list(size):
    s = set()
    ans = []
    while True:
        s.add(random.randint(1, 5 * size))
        if (len(s) == size):
            break

    for num in s:
        ans.append(num)
    return ans


def inorder_traversal(L, node):
    if node == None:
        return
    inorder_traversal(L, node.left)
    L.append(node.value)
    inorder_traversal(L, node.right)


def preorder_traversal(L, node):
    if node == None:
        return
    L.append(node.value)
    preorder_traversal(L, node.left)
    preorder_traversal(L, node.right)

def postorder_traversal(L, node):
    if node == None:
        return
    postorder_traversal(L, node.left)
    postorder_traversal(L, node.right)
    L.append(node.value)


def insertionTest(tree):
    numOfValues = 100
    RL = create_random_list(numOfValues)
    SL = RL.copy() ; SL.sort()

    for number in RL:
        tree.insert(number)

    inorderList = []
    inorder_traversal(inorderList, tree.root)
    
    if len(inorderList) != numOfValues:
        print("Insertion Test Failed")
        return

    allSame = all(inorderList[i] == SL[i] for i in range(numOfValues))

    if allSame:
        print("Insertion Test Passed")
    else:
        print("Insertion Test Failed")

def searchTest(tree):
    numOfValues = 100
    RL = create_random_list(numOfValues)
    randomNumber = random.choice(RL)
    
    for number in RL:
        tree.insert(number)
    
    if (tree.search(randomNumber) != None):
        print("Search Test Passed")
    else:
        print("Search Test Failed")

def deletionTest(tree):
    numOfValues = 100
    numOfDeletions = math.ceil(numOfValues * 0.1)
    RL = create_random_list(numOfValues)
    
    for number in RL:
        tree.insert(number)
    
    SL = RL.copy()
    
    deletions = []

    for _ in range(numOfDeletions):
        deletion = random.choice(SL)
        deletions.append(deletion)
        SL.remove(deletion)
    
    SL.sort()

    for number in deletions:
        tree.delete(number)
    
    inorderList = []

    inorder_traversal(inorderList, tree.root)

    if len(inorderList) != len(SL):
        print("Deletion Test Failed")
        return

    allSame = all(SL[i] == inorderList[i] for i in range(len(SL)))

    if allSame:
        print("Deletion Test Passed")
    else:
        print("Deletion Test Failed")
    



mytree = BST()
insertionTest(mytree)
mytree = BST()
searchTest(mytree)
mytree = BST()
deletionTest(mytree)