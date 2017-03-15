array = []
values = [12, 4, 5, 3, 8, 7]
for value in values:
    array.append(value)
    print(running_median(array))
    
import heapq

# max heap has smaller values 
# min heap has larger values 
# create max heap by using negative values

# default is min heap 
def running_median(array):
  upper_min_heap = []
  lower_max_heap = []
  for value in array:
    if len(min_heap) > len(max_heap):
      heapq.heappush(max_heap, value)
    else if  


array = []
values = [12, 4, 5, 3, 8, 7]
for value in values:
    array.append(value)
    print(running_median(array))
