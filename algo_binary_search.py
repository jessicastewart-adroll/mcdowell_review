# print cost positions
# index from 1

def find_flavors(fund, costs):
    for i, cost in enumerate(costs):
        if fund > cost and fund-cost in costs:
            return cost, fund-cost

t = int(input().strip())
for a0 in range(t):
    fund = int(input().strip())
    fund = int(input().strip())
    costs = list(map(int, input().strip().split(' ')))
    c1, c2 = find_flavors(fund, costs)
    print(c1, c2)
