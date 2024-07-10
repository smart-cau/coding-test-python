# https://www.acmicpc.net/problem/10971
# 외판원 순회2
# silver2
# re
import sys


N = int(sys.stdin.readline())
travel_costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_cost = sys.maxsize


def dfs(start, next, cost, visited):
    global min_cost
    if len(visited) == N:
        if travel_costs[next][start] != 0:
            min_cost = min(min_cost, cost + travel_costs[next][start])
        return

    for i in range(N):
        if travel_costs[next][i] != 0 and i not in visited and cost < min_cost:
            visited.append(i)
            dfs(start, i, cost + travel_costs[next][i], visited)
            visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])

print(min_cost)

