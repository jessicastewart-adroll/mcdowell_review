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
	
	from math import sqrt

def is_prime_sieve(n):
	if n < 2:
		print('Not prime')
		return

	def get_primes(n):
		stop = int(sqrt(n))
		sieve = [True for i in range(2, stop+1)]

		i = 2
		while i*i < len(sieve):
			j = i
			while i*j < len(sieve)+2:	
				mark = (i*j)-2
				sieve[mark] = False
				j+=1
			i+=1
		
		return [i for i in range(2, stop+1) if sieve[i-2]]	
		
	primes = get_primes(n)
	for prime in primes:
		if not n%prime:
			print('Not prime')
			return
	print('Prime')	
    
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    is_prime_sieve(n)
    
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    is_prime_sqrt(n)
    is_prime_sieve(n)
