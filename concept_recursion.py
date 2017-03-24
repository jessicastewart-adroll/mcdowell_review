'''
step increments 1, 2, 3
print number of ways

s -> number of staircases (1 to 5)
n -> height of staircase (1 to 36)

1 -> 1
3 -> 4
7 -> 44
'''
def possible_climbs(staircase):
	steps = [1, 2, 3]
	trips = []

	for step in steps:
		if step == 1:
			trips.append([1]*staircase)
		else:
			i = 1
			while staircase - (step*i) > 0:
				i+=1

def check_and_subtract(height, step):
	if step > height return height

	i = 1
	while height - (step*i) > 0:
		i += 1

	return height - (step*i)


possible_climbs(1)	
possible_climbs(4)	
possible_climbs(44)		
