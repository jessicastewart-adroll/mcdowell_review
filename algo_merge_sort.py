### final ### https://www.quora.com/How-can-I-efficiently-compute-the-number-of-swaps-required-by-slow-sorting-methods-like-insertion-sort-and-bubble-sort-to-sort-a-given-array
def merge(left, right):
    result = []
    i, j, inversions = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            inversions += j
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    inversions += j*(len(left)-i)
    result += left[i:]
    result += right[j:]
    return inversions, result

def merge_sort(A):
    if len(A) <= 1:
        return 0, A
    middle = len(A)//2
    left_inversions, left = merge_sort(A[:middle])
    right_inversions, right = merge_sort(A[middle:])
    merge_inversions, merged = merge(left, right)
    inversions = left_inversions + right_inversions + merge_inversions
    return inversions, merged

def count_inversions(arr):
    inversions, sorted_arr = merge_sort(arr)
    print(inversions)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    count_inversions(arr)

######

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
