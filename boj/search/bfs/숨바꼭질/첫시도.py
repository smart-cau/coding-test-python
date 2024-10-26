# https://www.acmicpc.net/problem/1679
# 숨바꼭질
# silver 1
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]


def bfs(position):
    queue = deque([(position, 0)])

    while queue:
        node, time = queue.popleft()
        visited[node] = True
        if node == k:
            return time

        neighbors = [node - 1, node + 1, node * 2]
        time += 1

        for neighbor in neighbors:
            if 0 <= neighbor < 100001 and not visited[neighbor]:
                queue.append((neighbor, time))


print(bfs(n))
