# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
# silver 1
import sys

number_count = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split())) # +, -, *, //

maximum = -sys.maxsize
minimum = sys.maxsize


def backtracking(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == number_count:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus:
        backtracking(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        backtracking(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        backtracking(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        backtracking(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)


backtracking(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(maximum)
print(minimum)