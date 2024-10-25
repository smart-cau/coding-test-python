# https://www.acmicpc.net/problem/2644
# 촌수계산
# silver 2
import sys

family_count = int(sys.stdin.readline())
first_parent, target = map(int, sys.stdin.readline().split())
relation_count = int(sys.stdin.readline())

graph = [[] for _ in range(family_count + 1)]

for _ in range(relation_count):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [0 for _ in range(family_count + 1)]


def dfs(node, count):
    visited[node] = count
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, count + 1)


dfs(first_parent, 1)
print(visited[target] if visited[target] > 0 else -1)
