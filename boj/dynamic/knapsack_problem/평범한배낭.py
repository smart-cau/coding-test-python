# https://www.acmicpc.net/problem/12865
# 평범한 배낭
# gold 5
# re
import sys

input = sys.stdin.readline

item_count, max_weight = map(int, input().split())
items = [[]]
for _ in range(item_count):
    weight_i, value_i = map(int, input().split())
    items.append([weight_i, value_i])

dp = [[0] * (max_weight + 1) for _ in range(item_count + 1)]

for nth in range(1, item_count + 1):
    for weight in range(1, max_weight + 1):
        weight_i, value_i = items[nth]
        dp_value = None
        if weight_i > weight:
            dp_value = dp[nth - 1][weight]
        else:
            dp_value = max(dp[nth - 1][weight], dp[nth - 1][weight - weight_i] + value_i)
        dp[nth][weight] = dp_value

print(dp[item_count][max_weight])
