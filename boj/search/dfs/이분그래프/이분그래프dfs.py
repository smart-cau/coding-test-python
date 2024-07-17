# https://www.acmicpc.net/problem/1707
# 이분그래프
# gold 4
import sys
sys.setrecursionlimit(10 ** 9)
test_count = int(sys.stdin.readline())


def is_bipartite(graph):
    vertex_count = len(graph)
    visited = [None] * len(graph)

    def get_color(level):
        return 'RED' if level % 2 == 0 else 'BLACK'

    def dfs(start, level):
        visited[start] = get_color(level)
        neighbors = graph[start]
        for neighbor in neighbors:
            if visited[neighbor] is None:
                dfs(neighbor, level + 1)

    for i in range(1, vertex_count):
        if visited[i] is None:
            dfs(i, 1)

    for i in range(1, len(graph)):
        for neighbor in graph[i]:
            if visited[i] == visited[neighbor]:
                return "NO"

    return "YES"


for _ in range(test_count):
    vertex_count, edge_count = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(vertex_count + 1)]
    for _ in range(edge_count):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(is_bipartite(graph))
