# https://www.acmicpc.net/problem/9461
# 파도반 수열
# silver 3
import sys

input = sys.stdin.readline

test_cases_count = int(input())

for _ in range(test_cases_count):
    n = int(input())
    dp = [1] * (n + 1)
    dp[0] = 0
    if n < 3:
        print(dp[n])
        continue
    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[n])
