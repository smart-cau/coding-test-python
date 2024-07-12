# https://www.acmicpc.net/problem/1110
# 더하기 사이클
# bronze 1
N = int(input())

count = 0
a, b = first, second = N // 10, N % 10

while True:
    count += 1
    """
    temp = a
    a = b
    b = (temp + b) % 10
    """
    a, b = b, (a + b) % 10

    if a == first and b == second:
        break

print(count)
