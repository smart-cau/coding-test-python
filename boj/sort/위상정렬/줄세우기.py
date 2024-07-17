# https://www.acmicpc.net/problem/2252
# 줄 세우기
# gold 3
import sys
from collections import deque

student_count, compare_count = map(int, sys.stdin.readline().split())

compares = [[] for _ in range(student_count + 1)]
indegree = [0] * (student_count + 1)

for _ in range(compare_count):
    start, end = map(int, sys.stdin.readline().split())
    compares[start].append(end)
    indegree[end] += 1


def topological_sort():
    result = []
    queue = deque()

    for i in range(1, student_count + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in compares[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


print(*topological_sort(), sep=' ')
