'''
step increments 1, 2, 3
print number of ways

s -> number of staircases (1 to 5)
n -> height of staircase (1 to 36)

1 -> 1
3 -> 4
7 -> 44
'''
def climb_permutations(n, counts={}):
	STEPS = [3, 2, 1]

	if n < 0:
		return 0
	if n <= 1:
		return 1

	total = 0
	for step in STEPS:
		if not counts.get(n-step):
			counts[n-step] = climb_permutations(n-step, counts)
		total += counts[n-step]   
	return total

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(climb_permutations(n))
