# performant 
#!/bin/python3
import sys
import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
  a_t = int(input().strip())
  bisect.insort(a, a_t)
  mid = len(a)//2
  if len(a)%2:
    print(float(a[mid]))
  else:
    print(float((a[mid]+a[mid-1])/2))

######################
import heapq

def running_median(array):
  if not array:
    return
  if len(array) < 2:
    return float(array[0])
    
  lower = []
  upper = []
  for value in array:
    if len(lower) <= len(upper):
      heapq.heappush(lower, -value)
    else:
      heapq.heappush(upper, value)
    
    if lower and upper:  
      if -lower[0] > upper[0]:
        first = -heapq.heappop(lower)
        second = heapq.heappop(upper)
        heapq.heappush(lower, -second)
        heapq.heappush(upper, first)
        
  #print(lower, upper)      
        
  if len(lower) == len(upper):
    first = -heapq.heappop(lower)
    second = heapq.heappop(upper)
    return float((first+second)/2)
  elif len(lower) > len(upper): 
    return float(-heapq.heappop(lower))
  else: 
    return float(heapq.heappop(upper))
  
print(running_median([12]))
print(running_median([12, 4]))
print(running_median([12, 4, 5]))
print(running_median([12, 4, 5, 3]))
print(running_median([12, 4, 5, 3, 8]))
print(running_median([12, 4, 5, 3, 8, 7]))
