def merge(array, helper, start, mid, end):
	for i in range(start, end+1):
		helper[i] = array[i]
	current = start
	left = start
	right = mid + 1

	while left <= mid and right <= end:
		if helper[left] <= helper[right]:
			current += 1
			left += 1
			array[current] = helper[left]
		else:
			swaps += mid + 1 - left
			current += 1
			right += 1
			array[current] = helper[right]	

	while left <= mid:
		current += 1
		left += 1
		array[current] = helper[left]

def merge_sort(array, helper, start, end):
	if start < end:
		mid = (start + end) // 2
		merge_sort(array, helper, start, mid)
		merge_sort(array, helper, mid+1, end)
		merge(array, helper, start, mid, end)

def count_inversions(array):
	helper = []
	merge_sort(array, helper, 0, len(array)-1)	
  
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
