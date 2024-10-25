# https://www.acmicpc.net/problem/2644
# 촌수계산
# silver 2
import sys
from collections import deque

family_count = int(sys.stdin.readline())
first_parent, target = map(int, sys.stdin.readline().split())
relation_count = int(sys.stdin.readline())

graph = [[] for _ in range(family_count + 1)]

for _ in range(relation_count):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [0 for _ in range(family_count + 1)]


def bfs(parent):
    queue = deque()
    queue.append(parent)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if visited[child] == 0:
                visited[child] = visited[node] + 1 # 여기가 중요!! visited[child] += 1이 아님
                queue.append(child)


bfs(first_parent)
print(visited[target] if visited[target] > 0 else -1)
