"""
Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
less than on LEFT
greather than on RIGHT
*helper functions
*CANNOT have duplicates in binary search tree
input: root node
output: True/False
"""
class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree(root):
    return check(root, float('inf'), float('-inf'))    

def check(node, pos_inf, neg_inf):
    if not node:
        return True
    
    if node.left > node.data or node.right < node.data:
        return False
    
    return check(node.left) and check(node.right)


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

root = four
root.left = three
root.right = five
three.left = one
three.right = two
five.right = six
six.right = seven
