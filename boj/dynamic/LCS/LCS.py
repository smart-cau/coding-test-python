# https://www.acmicpc.net/problem/9251
# LCS
# gold 5
import sys

input = sys.stdin.readline

str_a = input().rstrip()
str_b = input().rstrip()

dp = [[0] * (len(str_b) + 1) for _ in range(len(str_a) + 1)]

for i in range(1, len(str_a) + 1):
    for j in range(1, len(str_b) + 1):
        if str_a[i - 1] == str_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(str_a)][len(str_b)])
