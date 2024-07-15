# https://www.acmicpc.net/problem/11724
# 연결요소의 개수
# silver 2
import sys

vertex_count, edge_count = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vertex_count + 1)]

for _ in range(edge_count):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = []


def dfs(vertex):
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor)


count = 0

for i in range(1, vertex_count + 1):
    if i not in visited:
        count += 1
        dfs(i)

print(count)
