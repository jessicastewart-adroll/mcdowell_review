class Node:
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

binary_tree = four
binary_tree.left = three
binary_tree.right = five
three.left = one
three.right = two
five.right = six
six.right = seven

duplicate_tree = four
duplicate_tree.left = three
duplicate_tree.right = five
three.left = one
three.right = three
five.right = six
six.right = seven

broken_tree = four
broken_tree.left = three
broken_tree.right = five
three.left = one
three.right = two
five.left = six
five.right = seven
