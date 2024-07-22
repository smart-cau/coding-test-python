# https://www.acmicpc.net/problem/9084
# 동전
# gold 5
# re
import sys

input = sys.stdin.readline

test_count = int(input())
result = []
for _ in range(test_count):
    coin_type_count = int(input())
    coins = [0, *list(map(int, input().split()))]
    total_amount = int(input())

    dp = [[0 for _ in range(total_amount + 1)] for _ in range(coin_type_count + 1)]

    for coin_idx in range(1, coin_type_count + 1):
        coin = coins[coin_idx]
        for amount in range(1, total_amount + 1):
            if coin_idx == 1:
                dp[coin_idx][amount] = 1 if amount % coin == 0 else 0
                continue

            dp_value = None
            if coin > amount:
                dp_value = dp[coin_idx - 1][amount]
            if coin == amount:
                dp_value = dp[coin_idx - 1][amount] + 1
            if coin < amount:
                dp_value = max(dp[coin_idx - 1][amount],
                               dp[coin_idx - 1][amount] + dp[coin_idx][amount - coin])

            dp[coin_idx][amount] = dp_value

    result.append(dp[coin_type_count][total_amount])

print(*result, sep='\n')
