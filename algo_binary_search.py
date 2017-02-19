from functools import cmp_to_key

class Flavor(object):
    def __init__(self, position, cost):
        self.position = position
        self.cost = cost
        
    def __repr__(self):
        return 'Flavor ${} at {}'.format(self.cost, self.position)
    
    def comparator(a, b):
        return a.cost - b.cost
        
def get_flavors(a):
    flavors = []   
    for i, c in enumerate(a):
        flavors.append(Flavor(i+1, c))
        
    return flavors  

def binary_search(array, left, right, value):
    while left <= right:
        mid = left+(right-left)//2
        if array[mid].cost == value:
            return array[mid].position
        elif array[mid].cost > value:
            right = mid - 1
        elif array[mid].cost < value: 
            left = mid + 1
    
    else:
        return -1

def get_flavor_pair(flavors, money):
    for flavor in flavors:
        cost_one = flavor.cost
        cost_two = money-flavor.cost
        if cost_two > 0:
            result = binary_search(flavors, 0, len(flavors)-1, cost_two)
            if result > -1:
                print(min(flavor.position, result), max(flavor.position, result))
                return
        else:
            return
            
t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    flavors = get_flavors(a) 
    flavors = sorted(flavors, key=cmp_to_key(Flavor.comparator))
    pair = get_flavor_pair(flavors, m)
