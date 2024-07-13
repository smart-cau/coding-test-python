# https://www.acmicpc.net/problem/3055
# 탈출
# gold 4
# re
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

start = end = None
forest = [[] for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
waters = []
BIEBER = 'D'
HEDGEHOG = 'S'
ROCK = 'X'
WATER = '*'

for i in range(R):
    line = sys.stdin.readline().strip()
    for j in range(C):
        c = line[j]
        if c == HEDGEHOG:
            start = [i, j]
            visited[i][j] = 0
        if c == WATER: waters.append([i, j])
        forest[i].append(c)


def escape(start):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def is_next_cell_movable(ny, nx, current):
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            return False
        if visited[ny][nx] != -1: return False
        next = forest[ny][nx]
        if next == ROCK:
            return False
        if next == WATER:
            return False
        if current == WATER and next == BIEBER:
            return False
        return True

    queue = deque()

    for i in range(len(waters)):
        queue.append(waters[i])
    queue.append(start)
    result = 0

    while queue:
        y, x = queue.popleft()
        current = forest[y][x]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if is_next_cell_movable(ny, nx, current):
                if current == HEDGEHOG:
                    result += 1
                    if forest[ny][nx] == BIEBER:
                        return visited[y][x] + 1
                    visited[ny][nx] = visited[y][x] + 1
                forest[ny][nx] = current
                queue.append([ny, nx])

    return "KAKTUS"


print(escape(start))
