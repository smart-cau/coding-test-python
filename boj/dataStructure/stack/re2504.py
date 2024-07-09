# https://www.acmicpc.net/problem/2504
# 괄호의 값
# gold 5
# re
equation = input()

result = 0
temp = 1

stack = []

for i in range(len(equation)):
    next_p = equation[i]
    prev_p = equation[i - 1]

    if next_p == '(':
        stack.append(next_p)
        temp *= 2

    if next_p == '[':
        stack.append(next_p)
        temp *= 3

    if next_p == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break

        if prev_p == '(':
            result += temp
        temp //= 2
        stack.pop()

    if next_p == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if prev_p == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)

