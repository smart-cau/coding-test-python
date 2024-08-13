# https://www.acmicpc.net/problem/4803
# 트리
# gold 4
# re
from collections import deque
import sys


def getTreesCnt(graph, nodes):
    count = 0
    visited = [False] * (nodes + 1)    
    for node in range(1, nodes + 1):
        if not visited[node]:
            if bfs(node, graph, visited):
                count += 1
            
    return count

def bfs(start, graph, visited):
    queue = deque([(start, 0)]) # init parent = 0. deque에 초깃값는 디테일에서 계속 에러. 대괄호[] 소괄호()로 감싸야 함
    visited[start] = True
    visited_nodes, visited_edges = 0, 1

    while queue:
        node, parent = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            visited_edges += 1
            if visited[neighbor]:
                return False
            queue.append((neighbor, node))
            visited[neighbor] = True
            visited_nodes += 1
            
    return (visited_nodes - 1) == visited_edges

case_num = 0

while True:
    case_num += 1
    node_cnt, edge_cnt = map(int, sys.stdin.readline().split())
    if (node_cnt == edge_cnt == 0):
        break
    
    graph = []
    for i in range(node_cnt + 1):
        graph.append([])
    
    for _ in range(edge_cnt):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)


    tree_num = getTreesCnt(graph, node_cnt)

    if tree_num == 0:
        print(f"Case {case_num}: No trees.")
    if tree_num == 1:
        print(f"Case {case_num}: There is one tree.")
    if tree_num > 1:
        print(f"Case {case_num}: A forest of {tree_num} trees.")
