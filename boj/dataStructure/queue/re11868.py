# https://www.acmicpc.net/problem/11868
# 요세푸스 문제 0
# silver 5
# re
import sys

n, k = map(int, sys.stdin.readline().split())


class Yose:
    def __init__(self, n, k):
        self.ptr = 0
        self.n = n
        self.k = k
        self.arr = [i for i in range(1, n + 1)]
        self.seq = []

    def pop(self):
        if len(self.arr) == 1:
            self.seq.append(self.arr.pop())
            return
        if self.ptr >= len(self.arr):
            self.ptr = 0

        next_ptr = self.ptr + self.k - 1
        if next_ptr >= len(self.arr):
            self.ptr = next_ptr - len(self.arr)
        else:
            self.ptr = next_ptr

        self.seq.append(self.arr.pop(self.ptr))


yose = Yose(n, k)
for i in range(n):
    yose.pop()

arr = [i for i in range(1, n + 1)]
result = []
idx = 0

while arr:
    idx += (k - 1)
    idx = idx % len(arr)
    result.append(arr.pop(idx))

print('<', end="")
print(*result, sep=', ', end='>')
