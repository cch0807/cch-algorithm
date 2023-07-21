top = 4
cost = [10, 15, 20, 17, 1]
memo = {}


# top-down


# 시간복잡도 : O(n^2)
def dfs(n):
    if n == 0 and n == 1:
        return 0
    return min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])


# 시간복잡도 : O(n)
def dp(n):
    if n == 0 and n == 1:
        return 0
    if n not in memo:
        memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])

    return memo[n]


print(dp(top))

# bottom-up
