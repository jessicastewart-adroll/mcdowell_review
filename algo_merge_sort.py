# don't create new array for performance 

def mergeCount(A, B, count=0):
  C = []
  while A and B:
    if A[0] <= B[0]:
      C.append(A[0])
      A = A[1:]
    else:
      C.append(B[0])
      B = B[1:]
      count += 1
      
  if A:
    C.extend(A)
  if B:
    C.extend(B)
  return C, count
  
def merge_sort(input_list):
  if len(input_list) == 1:
    return input_list, 0
  
  mid = len(input_list)//2
  left, count_left = merge_sort(input_list[:mid])
  right, count_right = merge_sort(input_list[mid:])
  return mergeCount(left, right, count_left + count_right)
  
print(merge_sort([100, 3, -1, 4, -7]))
