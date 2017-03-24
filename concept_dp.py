'''
n -> total dollars
m -> dollar values (infinite amount of each)

'''
def single_denom(n, c):
	count = n//c

	total = [c]*count
	return total

# single_denom(10, 2)	
# single_denom(7, 2)	
# single_denom(1, 2)	

def get_change(n):
	coins = [2, 3, 1]
	result = []
	for c in coins:
		result += single_denom(n-sum(result), c)

	print(result)	

get_change(10)	
