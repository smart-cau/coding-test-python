# https://www.acmicpc.net/problem/1920
# 수 찾기
# silver 4
import sys


def binary_search(arr, target):
    pl, pr = 0, len(arr) - 1

    while True:
        mid = (pl + pr) // 2
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            pr = mid - 1
        if arr[mid] < target:
            pl = mid + 1
        if pl > pr:
            return 0


N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    print(binary_search(arr, target))
