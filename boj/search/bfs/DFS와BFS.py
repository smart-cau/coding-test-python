# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# silver 2
import sys
from collections import deque

vertex_count, edges_count, start_vertex = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vertex_count + 1)]

for _ in range(edges_count):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[start].sort()
    graph[end].append(start)
    graph[end].sort()

dfs_visited = []


def dfs(node):
    dfs_visited.append(node)
    neighbors = graph[node]
    for neighbor in neighbors:
        if neighbor not in dfs_visited:
            dfs(neighbor)


bfs_visited = []


def bfs(node):
    bfs_visited.append(node)
    queue = deque([node])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in bfs_visited:
                bfs_visited.append(neighbor)
                queue.append(neighbor)


dfs(start_vertex)
bfs(start_vertex)
print(*dfs_visited, sep=' ')
print(*bfs_visited, sep=' ')
