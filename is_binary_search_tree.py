class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_(root):
    return check(root, float('-inf'), float('inf'))

def check(node, tree_min, tree_max):
    if not node:
        return True

    if tree_min > node.data or tree_max < node.data:
        return False

    return check(node.left, tree_min, node.data-1) and check(node.right, node.data+1, tree_max)


one = Node(1)
two = Node(2)
three = Node(3)
three_duplicate = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

# working tree
binary_tree = three
binary_tree.left = two
binary_tree.right = four

# broken duplicate tree (use <, > rather than <=, >=) 
duplicate_tree = four
duplicate_tree.left = three
duplicate_tree.right = five
three.left = one
three.right = three_duplicate
five.right = six
six.right = seven

# another working tree
another_tree = four
another_tree.left = two
another_tree.right = six
two.left = one
two.right = three
six.left = five
six.right = seven

# broken tree that requires min/max values
broken_tree = three
broken_tree.left = two
broken_tree.right = five
two.left = one
two.right = four # can't be greater than root (3)
