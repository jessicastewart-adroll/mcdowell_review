def fibonacci(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not memo.get(n-1):
        memo[n-1] = fibonacci(n-1)
    if not memo.get(n-2):
        memo[n-2] = fibonacci(n-2)
    return memo[n-1] + memo[n-2]
n = int(input())
print(fibonacci(n))
