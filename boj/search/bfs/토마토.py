# https://www.acmicpc.net/problem/7569
# 토마토
# gold 5
from collections import deque
import sys

input = sys.stdin.readline
column, row, height = map(int, input().split())
graph = [[[0] * column for _ in range(row)] for _ in range(height)]

queue = deque()
should_chagne_num = 0
current_one_num = 0

for h in range(height):
    for r in range(row):
        inputs = list(map(int, input().split()))
        for c in range(column):
            graph[h][r][c] = inputs[c]
            if inputs[c] != -1:
                should_chagne_num += 1
            if inputs[c] == 1:
                queue.append([h, r, c])
                current_one_num += 1
            

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def is_in_bound(nh, nr, nc):
    if 0 <= nh < height and 0 <= nr < row and 0 <= nc < column:
        return True
    return False


def bfs():
    global current_one_num
    count = 0

    while should_chagne_num != current_one_num and queue:
        for _ in range(len(queue)):
            popped = queue.popleft()
            h, r, c = popped[0], popped[1], popped[2]
            for dh, dr, dc in directions:
                nh, nr, nc = h + dh, r + dr, c + dc
                if is_in_bound(nh, nr, nc) and graph[nh][nr][nc] == 0:
                    graph[nh][nr][nc] = 1
                    queue.append([nh, nr, nc])
                    current_one_num += 1
            
        count += 1
        
    if current_one_num != should_chagne_num:
        count = -1

    return count

print(bfs())