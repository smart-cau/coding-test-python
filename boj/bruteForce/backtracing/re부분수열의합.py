# https://www.acmicpc.net/problem/1182
# 부분수열의 합
# silver 2
# re
import sys


def combinations(arr, depth):
    def backtrack(start, path):
        if len(path) == depth:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            if not visited[i]:
                visited[i] = True
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()
                visited[i] = False

    result = []
    visited = [False] * len(arr)
    backtrack(0, [])
    return result


N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, N + 1):
    # print(combinations([j for j in range(N)], i))
    idx_combos = combinations([j for j in range(N)], i)
    for idxs in idx_combos:
        sum = 0
        for idx in idxs:
            sum += seq[idx]
        if sum == S:
            count += 1
print(count)
