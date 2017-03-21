from math import sqrt

def is_prime_sqrt(n):
	if n < 2:
		print('Not prime')
		return

	start = 2
	stop = sqrt(n)

	while start <= stop:
		if not n%start:
			print('Not prime')
			return
		start += 1	

	print('Prime')	
    
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    is_prime_sqrt(n)
#test_cases = [-1, 0, 2, 7, 50, 15]
#for n in test_cases:
#	is_prime_sqrt(n)
