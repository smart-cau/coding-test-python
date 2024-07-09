# https://www.acmicpc.net/problem/2493
# 탑
# gold 5
# re
import sys

n = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))

towers = []

for i in range(n):
    towers.append([i + 1, int(inputs[i])])

stack = []
result = []

for i in range(n):
    tower = towers[i]

    while stack:
        prev = stack[len(stack) - 1]

        if tower[1] > prev[1]:
            stack.pop()

        if tower[1] < prev[1]:
            result.append(prev[0])
            break

    if not stack:
        result.append(0)

    stack.append(tower)

print(*result)

