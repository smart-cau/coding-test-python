# https://www.acmicpc.net/problem/18258
# 큐2
# silver 4
import sys


class Queue:
    def __init__(self):
        self.__queue = []
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    def push(self, value):
        self.__queue.append(value)
        self.__rear += 1
        self.__size += 1

    def empty(self):
        return 1 if self.__size == 0 else 0

    def pop(self):
        if self.empty():
            return -1
        popped = self.__queue[self.__front]
        self.__front += 1
        self.__size -= 1
        return popped

    def size(self):
        return self.__size

    def front(self):
        if self.empty():
            return -1
        return self.__queue[self.__front]

    def back(self):
        if self.empty():
            return -1
        return self.__queue[self.__rear]


n = int(sys.stdin.readline())
inputs = [sys.stdin.readline().split() for _ in range(n)]

queue = Queue()

for input in inputs:
    inst = input[0]

    if inst == 'push':
        value = int(input[1])
        queue.push(value)

    if inst == 'pop':
        print(queue.pop())

    if inst == 'size':
        print(queue.size())

    if inst == 'empty':
        print(queue.empty())

    if inst == 'front':
        print(queue.front())

    if inst == 'back':
        print(queue.back())

