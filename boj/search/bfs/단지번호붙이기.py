# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기
# silver 1
import sys
from collections import deque

size = int(sys.stdin.readline())

graph = [[] for _ in range(size)]
for i in range(size):
    row = sys.stdin.readline().strip()
    for j in range(size):
        graph[i].append(int(row[j]))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start_row, start_col):
    visited[start_row][start_col] = True
    count = 0
    queue = deque()
    queue.append([start_row, start_col])

    while queue:
        y, x = queue.popleft()
        count += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < size and 0 <= nx < size:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append([ny, nx])
                    visited[ny][nx] = True
            else:
                continue

    result.append(count)


visited = [[False] * size for _ in range(size)]
result = []

for i in range(size):
    for j in range(size):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

result.sort()
print(len(result))
print(*result, sep='\n')
