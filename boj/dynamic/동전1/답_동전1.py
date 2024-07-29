# https://velog.io/@jxlhe46/백준-2293번.-동전-1-bfi120m5
import sys

input = sys.stdin.readline

coin_count, total_amount = map(int, input().split())
coins = [int(input()) for _ in range(coin_count)]

dp = [0] * (total_amount + 1)
dp[0] = 1

# 기존 코드에서 2차원을 1차원으로 압축한 내용
for coin in coins:
    for i in range(coin, total_amount + 1):
        dp[i] += dp[i - coin]

print(dp[total_amount])
