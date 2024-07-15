# https://www.acmicpc.net/problem/2606
# 바이러스
# silver 3
import sys

computer_count = int(sys.stdin.readline())
network_count = int(sys.stdin.readline())

nets = [[] for _ in range(computer_count + 1)]

for _ in range(network_count):
    start, end = map(int, sys.stdin.readline().split())
    nets[start].append(end)
    nets[end].append(start)

visited = []
count = 0


def dfs(node):
    global count
    visited.append(node)
    neighbors = nets[node]
    for neighbor in neighbors:
        if neighbor not in visited:
            count += 1
            dfs(neighbor)


dfs(1)
print(count)