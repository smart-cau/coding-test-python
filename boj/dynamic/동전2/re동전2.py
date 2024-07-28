# https://www.acmicpc.net/problem/2294
# 동전 2
# gold 5
# re -> 계속 시간초과 나는 코드
import sys

input = sys.stdin.readline

coin_types_count, total_amount = map(int, input().split())

coins = set()
coins.add(0)
for _ in range(coin_types_count):
    coin = int(input())
    if total_amount > coin:
        coins.add(coin)

coins = sorted([*list(coins)])
coin_count = len(coins)

if min(coins) > total_amount:
    print(-1)
    exit(0)

INF = 10e7

dp = [[INF] * (total_amount + 1) for _ in range(coin_count)]

for coin_idx in range(1, coin_count):
    for amount in range(coins[1], total_amount + 1):
        if coins[coin_idx] > amount:
            dp[coin_idx][amount] = dp[coin_idx - 1][amount]
        if coins[coin_idx] <= amount:
            if amount % coins[coin_idx] == 0:
                dp[coin_idx][amount] = amount // coins[coin_idx]
            else:
                quotient = amount // coins[coin_idx]
                mod = amount % coins[coin_idx]
                min_mod = INF
                for i in range(1, coin_count):
                    min_mod = min(min_mod, dp[i][mod])
                dp[coin_idx][amount] = quotient + min_mod

result = INF
for i in range(1, coin_count):
    result = min(result, dp[i][total_amount])

print(result if result != INF else -1)
