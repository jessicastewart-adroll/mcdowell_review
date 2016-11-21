'''
*sort increasing 
*even number of inputs -> get average

input -> integer
output -> print integer rounded to 10th decimal 

HEAP
  min - root node smallest
  max - root node largest
  sorted top-to-bottom, left-to-right (complete tree)
  insert: first available leaf then bubble up, if replace root then put at leaf and bubble up
  implementation: NOT NODES, indexed arrays
    0 index is root
    parent = (index-2)/2
    left = (index * 2) + 1
    right = (index * 2) + 2
    *peek
      returns first element (root)
    *poll
      returns first element (root) and removes
    *add
      add element to heap
      add to root leaf
      heapifyUp
    *heapifyUp
    *heapifyDown
'''
