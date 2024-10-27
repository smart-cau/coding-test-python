# https://www.acmicpc.net/problem/1303
# 전쟁-전투
# silver 1
import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split(' '))

MINE = 'W'
ENEMY = 'B'

graph = []
for _ in range(row):
    line = list(sys.stdin.readline().strip())
    graph.append(line)

visited = [[False] * col for _ in range(row)]
queue = deque()

dm = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = [0, 0] # W, B

def bfs(r, c):
    count = 0
    queue.append((r, c))
    char = graph[r][c]
    visited[r][c] = True

    while queue:
        y, x = queue.popleft()        
        count += 1
        
        for (dy, dx) in dm:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < row and 0 <= nx < col:
                if graph[ny][nx] == char and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    
    if char == MINE:
        result[0] += count ** 2

    if char == ENEMY:
        result[1] += count ** 2
    

for i in range(row):
    for j in range(col):
        if not visited[i][j]:            
            bfs(i, j)

print(result[0], result[1])