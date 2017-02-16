# print cost positions
# index from 1

def find_pair_position(pair, costs):
    for i, cost in enumerate(costs):

t = int(input().strip())
for a0 in range(t):
    fund = int(input().strip())
    flavors = int(input().strip())
    costs = list(map(int, input().strip().split(' ')))
    
    for i, cost in enumerate(costs):
        if fund > cost:
            pair_position = find_pair_position(fund-cost, costs)
            if pair_position:
                print(i+1, pair_position)

def binary_search(values, to_find, count=0):
	mid = len(values)//2

	if values[mid] == to_find:
		return mid + count
	elif values[mid] < to_find:
		binary_search(values[mid+1:], to_find, mid)
	elif values[mid] > to_find:
		binary_search(values[:mid], to_find)

	return -1
