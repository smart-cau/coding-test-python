# https://www.acmicpc.net/problem/10971
# 외판원 순회2
# silver2
import sys

N = int(sys.stdin.readline())

travel_costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_cost = sys.maxsize
visited = [False] * N


def dfs(origin, _from, cost, count):
    global min_cost
    visited[_from] = True

    if count == N - 1:
        if travel_costs[_from][origin] != 0:
            min_cost = min(min_cost, cost + travel_costs[_from][origin])
        return

    for i in range(N):
        if not visited[i] and travel_costs[_from][i] != 0 and cost < min_cost:
            visited[i] = True
            dfs(origin, i, cost + travel_costs[_from][i], count + 1)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 0)
    visited[i] = False

print(min_cost)

