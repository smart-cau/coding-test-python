# https://www.acmicpc.net/problem/18352
# 특정거리의 도시찾기
# silver 2
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
INF = 1e8

graph = [[] for _ in range(N + 1)]
distances = [0] * (N + 1)

for _ in range(M):
    start, dest = map(int, sys.stdin.readline().split())
    graph[start].append(dest)


def bfs_path(graph, start):
    queue = deque([start])
    visited = set()

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        current_distance = distances[vertex]
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                distances[neighbor] = current_distance + 1
                visited.add(neighbor)
                queue.append(neighbor)

    return distances


def get_cities(distances):
    result = []
    for i in range(1, N + 1):
        if distances[i] == K:
            result.append(i)
    return result


result = get_cities(bfs_path(graph, X))

if result:
    print(*result, sep='\n')

else:
    print(-1)

