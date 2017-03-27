### recursive 
def make_change(total, coins):
	if total == 0:
		return 1

	if total < 0:
		return 0

	if not coins:
		return 0

	return make_change(total-coins[0], coins) + make_change(total, coins[1:])

print(make_change(4, [1, 2,3]))
