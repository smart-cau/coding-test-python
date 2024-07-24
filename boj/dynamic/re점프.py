# https://www.acmicpc.net/problem/2253
# 점프
# gold 4
# re
import sys

input = sys.stdin.readline

stone_count, small_stones_count = map(int, input().split())
max_speed = int((2 * stone_count) ** 0.5) + 1
small_rocks = [False] * stone_count
for _ in range(small_stones_count):
    small_rocks[int(input()) - 1] = True

dp = [[stone_count] * max_speed for _ in range(stone_count)]
if not small_rocks[1]:
    dp[1][0] = 1
for nth_stone in range(1, stone_count - 1):
    if small_rocks[nth_stone]:
        continue
    for speed in range(max_speed):
        if dp[nth_stone][speed] == stone_count:
            continue
        for next_speed in [speed - 1, speed, speed + 1]:
            next_stone = nth_stone + next_speed + 1
            if (-1 < next_speed < max_speed and next_stone < stone_count and
                    not small_rocks[nth_stone + next_speed + 1]):
                dp[next_stone][next_speed] = min(dp[nth_stone][speed] + 1,
                                                 dp[next_stone][next_speed])

answer = min(dp[-1])
print(answer if answer < stone_count else -1)
