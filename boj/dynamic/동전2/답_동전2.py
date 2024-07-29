import sys

input = sys.stdin.readline

coin_count, total_amount = map(int, input().split())

coins = set(int(input()) for _ in range(coin_count))
coins = sorted(list(coins))
coin_count = len(coins)

INF = 10e7

dp = [INF] * (total_amount + 1)
dp[0] = 0

for coin in coins:
    for amount in range(coin, total_amount + 1):
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)

print(dp[total_amount] if dp[total_amount] != INF else -1)
