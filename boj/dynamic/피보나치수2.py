# https://www.acmicpc.net/problem/2478
# 피보나치수 2
# bronze 1
import sys

target = int(sys.stdin.readline())


def tabulation(target):
    dp = [0] * (target + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, target + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[target]


def memoization(target):
    dp = [0] * (target + 1)

    def memo(num):
        if num <= 1:
            return num
        if dp[num] != 0:
            return dp[num]
        dp[num] = memo(num - 1) + memo(num - 2)
        return dp[num]

    return memo(target)


print(memoization(target))