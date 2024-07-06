# https://www.acmicpc.net/problem/1913
# 하노이의 탑
# gold 5
# re
import sys

height = int(sys.stdin.readline())

print(2 ** height - 1)


def move(num, x, y):
    # 1st to 2nd
    if num > 1:
        move(num - 1, x, 6 - x - y)

    # 실제로 옮기는 부분

    print(f"{x} {y}")

    # 2nd to 3rd
    if num > 1:
        move(num - 1, 6 - x - y, y)


if height <= 20:
    move(height, 1, 3)
