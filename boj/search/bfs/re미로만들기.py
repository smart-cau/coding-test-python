# https://www.acmicpc.net/problem/2665
# 미로 만들기
# gold 4
# re
import sys
from collections import deque

SIZE = int(sys.stdin.readline())

maze = [[int(digit) for digit in sys.stdin.readline().strip()] for _ in range(SIZE)]

PATH = 1
BLOCK = 0


def bfs(maze):
    visited = [[-1] * SIZE for _ in range(SIZE)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 0
    # 하 우 상 좌
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()
        if x == SIZE - 1 and y == SIZE - 1:
            return visited[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < SIZE and 0 <= nx < SIZE and visited[ny][nx] == -1:
                if maze[ny][nx] == PATH:
                    queue.appendleft([ny, nx]) # path 먼저 우선순위로 탐색
                    visited[ny][nx] = visited[y][x]
                if maze[ny][nx] == BLOCK:
                    queue.append([ny, nx]) # 근처에 있는 block들도 큐에 넣기는 함. 하지만 낮은 우선순위!
                    visited[ny][nx] = visited[y][x] + 1


print(bfs(maze))
