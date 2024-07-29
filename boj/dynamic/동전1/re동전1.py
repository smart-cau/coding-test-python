# https://www.acmicpc.net/problem/2293
# 동전 1
# gold 5
# re -> 메모리 초과... 정답은 나옴
import sys

input = sys.stdin.readline

coin_count, total_amount = map(int, input().split())

coins = set()
coins.add(0)
for _ in range(coin_count):
    coin = int(input())
    if coin < total_amount:
        coins.add(coin)

coins = sorted(list(coins))
coin_count = len(coins)

dp = [[0] * (total_amount + 1) for _ in range(coin_count)]

for i in range(1, coin_count):
    for j in range(1, total_amount + 1):
        coin = coins[i]
        if coin > j:
            dp[i][j] = dp[i - 1][j]
        if coin == j:
            dp[i][j] = dp[i - 1][j] + 1
        if coin < j:
            dp[i][j] = dp[i - 1][j] + dp[i][j - coin]


print(dp[-1][-1])
