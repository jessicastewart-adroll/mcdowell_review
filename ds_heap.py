import heapq

def keep_even(array):
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
  
print(keep_even([12]))
print(keep_even([12, 4]))
print(keep_even([12, 4, 5]))
print(keep_even([12, 4, 5, 3]))
print(keep_even([12, 4, 5, 3, 8]))
print(keep_even([12, 4, 5, 3, 8, 7]))
