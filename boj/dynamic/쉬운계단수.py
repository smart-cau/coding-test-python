# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수
# silver 1
import sys

n = int(sys.stdin.readline())

dp = [[0] * (10) for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

mod_num = 1000000000
for row in range(2, n + 1):
    for column in range(10):
        if column == 0:
            dp[row][column] += dp[row - 1][1]
            continue
        if column == 9:
            dp[row][column] += dp[row - 1][8]
            continue
        dp[row][column] = dp[row - 1][column + 1] + dp[row - 1][column -1]
        dp[row][column] %= mod_num

    
print(sum(dp[n]) % mod_num)
