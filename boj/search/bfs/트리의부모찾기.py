# https://www.acmicpc.net/problem/11725
# 트리의 부모찾기
# silver 2
import sys
from collections import deque

vertex_count = int(sys.stdin.readline())

tree = [[] for _ in range(vertex_count + 1)]

parents_of = [-1] * (vertex_count + 1)

for _ in range(vertex_count - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs():
    parents_of[1] = 0
    queue = deque([1])

    while queue:
        node = queue.popleft()
        children = tree[node]
        for child in children:
            if parents_of[child] == -1:
                parents_of[child] = node
                queue.append(child)


bfs()
print(*parents_of[2:], sep='\n')
sys.stdin.close()
