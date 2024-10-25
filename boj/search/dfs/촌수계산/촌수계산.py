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

visited = []

found = False


def dfs(node, count):
    visited.append(node)
    if node == target:
        global found
        found = True
        print(count)
        return
    for i in graph[node]:
        if i not in visited:
            dfs(i, count + 1)


dfs(first_parent, 0)
if not found:
    print(-1)
