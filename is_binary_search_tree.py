# verify in-order traversal 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree(root):
    return check(root)

def check(node):
    if not node or (not node.left and not node.right):
        return True

    if node.left and not node.left.data < node.data:
        return False

    if node.right and not node.right.data > node.data:
        return False

    return check(node.left) and check(node.right)


one = Node(1)
two = Node(2)
three = Node(3)
three_duplicate = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

'''
binary_tree = three
binary_tree.left = two
binary_tree.right = four

duplicate_tree = four
duplicate_tree.left = three
duplicate_tree.right = five
three.left = one
three.right = three_duplicate
five.right = six
six.right = seven
'''

another_tree = four
another_tree.left = two
another_tree.right = six
two.left = one
two.right = three
six.left = five
six.right = seven
