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

TODO: fix return statements
"""

def check_binary_search_tree_(root):
    if root.data:
        print('root', root.data)
        continue_check(root)
    else:
        return True

def check_left(node):
    print('left check', node.data, node.left.data)
    if node.left.data >= node.data:
        return False
    else:
        continue_check(node.left)

def check_right(node):
    print('right check', node.data, node.right.data)
    if node.right.data <= node.data:
        return False
    else:
        continue_check(node.right)

def continue_check(node):
    if node.data and node.left:
        check_left(node)
        
    if node.data and node.right:
        check_right(node)   
