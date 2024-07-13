# https://www.acmicpc.net/problem/2178
# 미로탐색
# silver 1
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(N)]
visited = [[-1] * M for _ in range(N)]


PATH = 1
BLOCK = 0


def search_maze(maze):
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def is_movable(ny, nx):
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            return False
        if visited[ny][nx] != -1:
            return False
        if maze[ny][nx] == BLOCK:
            return False
        return True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_movable(ny, nx):
                if ny == N - 1 and nx == M - 1:
                    return visited[y][x] + 1
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])


print(search_maze(maze))
