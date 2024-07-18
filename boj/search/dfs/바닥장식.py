# https://www.acmicpc.net/problem/1388
# 바닥장식
# silver 4
import sys

sys.setrecursionlimit(10**6)
row_size, col_size = map(int, sys.stdin.readline().split())

graph = [sys.stdin.readline().strip() for _ in range(row_size)]

visited = [[False] * col_size for _ in range(row_size)]

_count = 0


def dfs(row, col, cell):
    count = 0
    visited[row][col] = True

    if cell == '-':
        if col + 1 >= col_size or graph[row][col + 1] == '|':
            return 1
        if col + 1 < col_size and graph[row][col + 1] == '-':
            if not visited[row][col + 1]:
                count += dfs(row, col + 1, graph[row][col + 1])

    if cell == '|':
        if row + 1 >= row_size or graph[row + 1][col] == '-':
            return 1
        if row + 1 < row_size and graph[row + 1][col] == '|':
            if not visited[row + 1][col]:
                count += dfs(row + 1, col, graph[row + 1][col])

    return count


for i in range(row_size):
    for j in range(col_size):
        if not visited[i][j]:
            _count += dfs(i, j, graph[i][j])

print(_count)
