# https://www.acmicpc.net/problem/1946
# 신입사원
# silver 1
import sys

input = sys.stdin.readline
test_cases = int(input())
results = []
for _ in range(test_cases):
    appliers = []
    applier_num = int(input())

    for _ in range(applier_num):
        first, second = map(int, input().split())
        appliers.append([first, second])
    appliers.sort()
    standard = appliers[0][1]
    count = 1
    last_idx = applier_num - 1
    for i in range(1, applier_num):
        if appliers[i][1] < standard:
            count += 1
            standard = appliers[i][1]

    results.append(count)

print(*results, sep='\n')
