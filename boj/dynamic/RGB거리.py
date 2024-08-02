# https://www.acmicpc.net/problem/1149
# RGB 거리
# silver 1
import sys

input = sys.stdin.readline

house_num = int(input())

cost = [list(map(int, input().split())) for _ in range(house_num)]

INF = 10e9

dp = [[INF] * 3 for _ in range(house_num)]

for i in range(3):
    dp[0][i] = cost[0][i]

for house in range(1, house_num):
    for color in range(3):
        for k in range(3):
            if k != color:
                dp[house][color] = min(dp[house][color], cost[house][color] + dp[house-1][k])

print(min(dp[-1]))
