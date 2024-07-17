# https://www.acmicpc.net/problem/2468
# 빙산
# gold 4
# re 답은 맞으나 시간초과
import sys
sys.setrecursionlimit(10**9)

row_size, col_size = map(int, sys.stdin.readline().split())

arctic_sea = [[] for _ in range(row_size)]
for y in range(row_size):
    row = list(map(int, sys.stdin.readline().split()))
    for x in range(col_size):
        arctic_sea[y].append(row[x])


def get_years():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    def after_year(graph, visited, y, x):
        around = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < row_size and 0 <= nx < col_size:
                if graph[ny][nx] == 0: around += 1

        visited[y][x] = (graph[y][x] - around)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if is_visitable(graph, visited, ny, nx):
                after_year(graph, visited, ny, nx)

    def decrease_height(graph, visited):
        for y in range(1, row_size - 1):
            for x in range(1, col_size - 1):
                decreased = visited[y][x]
                if decreased is not None:
                    graph[y][x] = decreased if decreased > 0 else 0

    def is_visitable(graph, visited, y, x):
        if 0 < y < row_size and 0 < x < col_size:
            if visited[y][x] is None and graph[y][x] != 0:
                return True
        return False

    def is_splitted(graph):
        def dfs(graph, visited, y, x):
            visited[y][x] = True
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if is_visitable(graph, visited, ny, nx):
                    dfs(graph, visited, ny, nx)

        visited = [[None] * col_size for _ in range(row_size)]
        splits = 0
        for y in range(1, row_size):
            for x in range(1, col_size):
                if is_visitable(graph, visited, y, x):
                    splits += 1
                    if splits > 1: return True
                    dfs(graph, visited, y, x)
        return False

    count = 0
    while True:
        melted_all = True
        decreased_heights = [[None] * col_size for _ in range(row_size)]
        for y in range(1, row_size):
            for x in range(1, col_size):
                if is_visitable(arctic_sea, decreased_heights, y, x):
                    count += 1
                    after_year(arctic_sea, decreased_heights, y, x)
                    decrease_height(arctic_sea, decreased_heights)
                    melted_all = False
                    if is_splitted(arctic_sea):
                        return count
        if melted_all:
            break
    return 0


print(get_years())
