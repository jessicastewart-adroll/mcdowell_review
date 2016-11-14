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
        continue_check(root)
    else:
        return True

def continue_check(node):
    if node.data and node.left:
        if node.left.data >= node.data:
            return False
        else:
            continue_check(node.left)
        
    if node.data and node.right:
        if node.right.data <= node.data:
            return False
        else:
            continue_check(node.right) 
