# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호
# silver 2
import sys

_input = sys.stdin.readline().strip()

num_str = ''
result = i = 0
temp = 0

while i < len(_input):
    c = _input[i]
    # 숫자 연결
    if c != '+' and c != '-':
        num_str += c
    if c == '+' or i == len(_input) - 1:
        result += int(num_str)
        num_str = ''
    if c == '-':
        if num_str:
            result += int(num_str)
        num_str = ''
        while True:
            j = i + 1
            if j == len(_input) or _input[j] == '-':
                if num_str:
                    temp += int(num_str)
                    num_str = ''
                result += (-1 * temp)
                temp = 0
                break
            c = _input[j]
            if c == '+':
                temp += int(num_str)
                num_str = ''
                i += 1
                continue
            # 숫자 연결
            num_str += c
            i += 1

    i += 1

print(result)
