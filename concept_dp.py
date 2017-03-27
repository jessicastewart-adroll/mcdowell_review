### recursive 
#!/bin/python3
import sys

def make_change(total, coins):
	if total == 0:
		return 1

	if total < 0:
		return 0

	if not coins:
		return 0

	return make_change(total-coins[0], coins) + make_change(total, coins[1:])
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(n, coins))

