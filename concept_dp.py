def make_change(total, coins, cache={}):
	if total == 0:
		return 0
	if total == 1:
		return 1

	result = 0
	for coin in coins:
		if not cache.get(total-coin):
			cache[total-coin] = make_change(total-coin, coins, cache)
		result += cache[total-coin]

	return result	

test_total = 4
test_coins = [1, 2, 3]
test_solution = 4

print(make_change(test_total, test_coins))
