def count_inversions(array):
  def merge(array, start, mid, end, temp):
    count = 0
    i = start
    j = mid + 1
    k = start
    while i <= mid or j <= end:
      if i > mid:
        k+=1
        j+=1
        array[k] = temp[j]
      elif j > end:
        k+=1
        i+=1
        array[k] = temp[i]
      elif temp[i] <= temp[j]:
        k+=1
        i+=1
        array[k] = temp[i]
      else:
        k+=1
        j+=1
        array[k] = temp[j]
        count += mid+1-i
    return count    
     
  
  def split(array, start, end, temp):
    if start >= end:
      return 0
      
    mid = start + (end - start) / 2 
    count = 0
    count += split(temp, start, mid, array)
    count += split(temp, mid+1, end, array)
    count += merge(array, start, mid, end, temp)
    
    return count
    
  temp = array[:]  
  return split(array, 0, len(array)-1, temp)
  
test_one = [1, 1, 1, 2, 2]  
test_two = [2, 1, 3, 1, 2]
test_three = [2, 1, 3, -11, -2]
#print(count_inversions(test_one))
print(count_inversions(test_two))
#print(count_inversions(test_three))
###
def count_inversions(array):
  def merge(left, right):
    swaps = 0
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        result.append(left[i])
        i+=1
      else:
        swaps += 1
        result.append(right[j])
        j+=1
    if i < len(left): 
      result.extend(left[i:])
      swaps += len(left[i:])
    if j < len(right): 
      result.extend(right[j:]) 
    print(left, right, swaps)
    return result  
    
  if len(array) <= 1:
    return array
  mid = len(array)//2
  left = count_inversions(array[:mid])
  right = count_inversions(array[mid:])
  return merge(left, right)
  
test_one = [1, 1, 1, 2, 2]  
test_two = [2, 1, 3, 1, 2]
test_three = [2, 1, 3, -11, -2]
#print(count_inversions(test_one))
print(count_inversions(test_two))
#print(count_inversions(test_three))

# don't create new array for performance 
def swap(array, a, b):
  array[a], array[b] = array[b], array[a]

def inplace_count(array, start_1, finish_1, start_2, finish_2, count=0):
  while start_1 <= finish_1 and start_2 <= finish_2:
    if array[start_1] >= array[start_2]:
      swap(array, start_1, start_2)
      start_1 += 1
      count += 1
    else:
      start_2 += 1
      
  return count
  
def inplace_sort(input_list, start, end):
  # break it down
  if end - start <= 1:
    return input_list
  
  mid = (end-start)//2
  count_left = inplace_sort(input_list, start, mid) # change
  count_right = inplace_sort(input_list, mid+1, end) # change
  
  # build it up
  return inplace_count(input_list, start, end, count_left + count_right)
  
print(inplace_sort([100, 3, -1, 4, -7]))

################################################
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
