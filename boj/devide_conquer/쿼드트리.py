# https://www.acmicpc.net/problem/1992
# 쿼드트리
# silver 1
import sys

N = int(sys.stdin.readline())

video = [input() for _ in range(N)]


def compress(arr):
    result = []
    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]
    size = len(arr)

    def is_same_color(y, x, size):
        color = arr[y][x]
        for i in range(y, y + size):
            for j in range(x, x + size):
                if color != arr[i][j]:
                    return False
        return True

    def dnc(y, x, step: int):
        color = arr[y][x]
        if is_same_color(y, x, step):
            result.append(color)
            return

        half = step // 2

        result.append('(')
        for i in range(len(dx)):
            dnc(y + dy[i] * half, x + dx[i] * half, half)
        result.append(')')

    dnc(0, 0, size)

    return result


print(*compress(video), sep='')
