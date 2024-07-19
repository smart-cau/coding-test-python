# https://www.acmicpc.net/problem/1904
# 01 타일
# silver 3
import sys

count = int(sys.stdin.readline())


def tile(target):
    dp = [0] * (target + 1)
    dp[0] = 0
    dp[1] = 1
    if target > 1:
        dp[2] = 2
        for i in range(3, target + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    return dp[target]


print(tile(count))
