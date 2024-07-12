# https://www.acmicpc.net/problem/2468
# 안전영역
# silver1
# re
import sys
from collections import deque

N = int(sys.stdin.readline())

area = []
max_h = -1
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        max_h = row[i] if row[i] > max_h else max_h
    area.append(row)

count = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, r):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1 # 해당 위치의 방문 표시

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우를 살펴봄
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 인접 영역에서 만약 방문 했거나, 지형이 비의 높이 r보다 작은 경우, 다음 for문으로
            if visited[nx][ny] == 1 or area[nx][ny] <= r:
                continue

            queue.append((nx, ny))
            visited[nx][ny]=1


res = 0
for r in range(max_h): # 비의 높이가 0~max_h일 때 탐색
    cnt = 0 # 비의 높이가 r일 때 안전영역의 개수
    visited = [[0]*N for _ in range(N)] # 비의 높이가 r일 때의 방문 처리 맵

    for i in range(N):
        for j in range(N):
            # 만약 지형이 비의 높이 r보다 높고, 방문하지 않은 영역에 대해서 bfs 수행
            if area[i][j] > r and visited[i][j] == 0:
                bfs(i, j, r)
                cnt += 1 # bfs 수행 후, 안전영역 + 1

    res = max(res, cnt) # 비의 높이가 0~max_h에서 안전 영역의 개수가 제일 많은 것 기록

print(res)
