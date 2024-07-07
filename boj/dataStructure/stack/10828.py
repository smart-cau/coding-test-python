# https://www.acmicpc.net/problem/10828
# 스택
# silver4
import sys


class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0
        self.__top = -1

    def push(self, val):
        self.__stack.append(val)
        self.__size += 1
        self.__top += 1

    def pop(self):
        if self.empty():
            return -1

        val = self.__stack[self.__top]
        del self.__stack[self.__top]
        self.__size -= 1
        self.__top -= 1
        return val

    def size(self):
        return self.__size

    def empty(self):
        return 1 if self.__size == 0 else 0

    def top(self):
        if self.empty():
            return -1
        return self.__stack[self.__top]


stack = Stack()
n = int(sys.stdin.readline())
inputs = [sys.stdin.readline() for _ in range(n)]
for i in range(n):
    input_ = inputs[i].split()
    instruction = input_[0]
    if instruction == 'push':
        stack.push(int(input_[1]))

    elif instruction == 'pop':
        print(stack.pop())

    elif instruction == 'size':
        print(stack.size())

    elif instruction == 'empty':
        print(stack.empty())

    elif instruction == 'top':
        print(stack.top())


