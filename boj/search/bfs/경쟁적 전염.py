# https://www.acmicpc.net/problem/18405
# 경쟁적 전염
# gold 5
import sys
from collections import deque

size, virus_range = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(size)]
init_viruses = []
for i in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(size):
        graph[i].append(row[j])
        if row[j] != 0:
            init_viruses.append((graph[i][j], i, j))

init_viruses.sort()

seconds, final_row, final_col = map(int, sys.stdin.readline().split())

visited = [[False] * size for _ in range(size)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

queue = deque(init_viruses)


time = 0
while time != seconds:
    for i in range(len(queue)):
        virus_num, y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < size and 0 <= nx < size:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    graph[ny][nx] = virus_num
                    queue.append((virus_num, ny, nx))

    time += 1

print(graph[final_row - 1][final_col - 1])
