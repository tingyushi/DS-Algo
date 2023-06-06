from rbt import RBTree
import random
import math


# create a random list with no repeated values
def create_random_list(size):
    s = set()
    while True:
        s.add(random.randint(1, 5 * size))
        if (len(s) == size):
            break
    return list(s)


# input: tree root node
# check if a red node has red children
def check_color(node):
    node_stack = []
    while (node != None or len(node_stack) != 0):
        while (node != None):
            node_stack.append(node)
            node = node.left
        if not (len(node_stack) == 0):
            node = node_stack.pop()
            if (node.is_red() and node.left != None and node.left.is_red()):
                return (False, "A red node has left red child")
            if (node.is_red() and node.right != None and node.right.is_red()):
                return (False, "A red node has right red child")
            node = node.right
    return (True, "PASS")


'''
leaves_list: an empty list to store all the leaf nodes
node: tree root
After running it, leaves_list should contain all the leaf nodes 
'''
def get_all_leaves(leaves_list, node):
    if node == None:
        return leaves_list
    node_stack = []
    while (node != None or len(node_stack) != 0):
        while (node != None):
            node_stack.append(node)
            node = node.left
        if not (len(node_stack) == 0):
            node = node_stack.pop()
            if (node.is_leaf()):
                leaves_list.append(node)
            node = node.right


'''
input: a leaf node
return the number of black nodes on the path from leaf node to the root
'''
def get_number_of_BNodes(node):
    counter = 0
    while (node != None):
        if not node.is_red():
            counter += 1
        node = node.parent
    return counter


# create tree 
tree1 = RBTree() ; tree2 = RBTree(); tree3 = RBTree()

# insert values
insertValuesSize = 1000
insertValues = create_random_list(insertValuesSize)
for number in insertValues:
    try:
        tree1.insert(number) ; tree2.insert(number) ;  tree3.insert(number)
    except:
        print("Insertion Error")
        exit()


print()

# check all paths have the same number of black nodes
print("=== Testing all the paths have the same number of black nodes ===")
leafNodes = []
BNodeNumber = []
get_all_leaves(leafNodes, tree1.root)

for leafNode in leafNodes:
    BNodeNumber.append( get_number_of_BNodes(leafNode) )

allSame = all(element == BNodeNumber[0] for element in BNodeNumber)

if (allSame):
    print("PASS")
else:
    print("FAIL")


print()

# check a red node should not have red children
print("=== Testing red nodes do not have red children ===")
result = check_color(tree2.root)
if (result[0]):
    print(result[1])
else:
    print("FAIL: " + result[1])

print()

# check height
print("=== Testing tree height ===")
maxHeight = math.ceil( math.log(insertValuesSize + 1, 2) ) * 2
if (tree3.get_height() <= maxHeight):
    print("PASS")
else:
    print("FAIL")

print()