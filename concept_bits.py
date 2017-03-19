a = [10, 10, 11, 12, 11]

def lonely_integer(a):
  cache = {}
  for num in a:
    if not cache.get(num):
      cache[num] = 1
    else: 
      cache[num] += 1
      
  for num in a:
    if cache[num] < 2:
      return num
  
print(lonely_integer(a))
