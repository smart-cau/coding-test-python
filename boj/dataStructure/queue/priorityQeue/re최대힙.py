# https://www.acmicpc.net/problem/11279
# 최대힙
# silver 2
# re 나중에 lib 없이 직접 구현해볼 것
import heapq
import sys

N = int(sys.stdin.readline())

max_heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        # python의 heaqp는 최소힙의 형태이므로 최대힙으로 값을 저장하기 위해 -1을 곱함
        print(heapq.heappop(max_heap) * - 1 if max_heap else 0)
    else:
        heapq.heappush(max_heap, num * - 1)
