# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기
# silver 1
import sys

number_count = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
inputs = list(map(int, sys.stdin.readline().split()))
operators = []
for i in range(len(inputs)):
    for j in range(inputs[i]):
        if i == 0: operators.append('+')
        if i == 1: operators.append('-')
        if i == 2: operators.append('*')
        if i == 3: operators.append('//')


def dfs(idx, visited, temp, result, depth):

    first_num = numbers[0] if depth == 0 else temp
    second_num = numbers[depth + 1]
    operator = operators[idx]

    if operator == '+':
        temp = (first_num + second_num)
    if operator == '-':
        temp = (first_num - second_num)
    if operator == '*':
        temp = (first_num * second_num)
    if operator == '//':
        if first_num * second_num < 0:
            temp = ((abs(first_num) // abs(second_num)) * -1)
        else:
            temp = (first_num // second_num)
    if depth == number_count - 2:
        result.append(temp)
        return
    for j in range(number_count - 1):
        if j not in visited:
            visited.append(j)
            # recc
            dfs(j, visited, temp, result, depth + 1)
            visited.pop()


result = []
for i in range(number_count - 1):
    visited = [i]
    dfs(i, visited, 0, result, 0)

print(max(result))
print(min(result))
