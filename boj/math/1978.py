# https://www.acmicpc.net/problem/1978
# 소수 찾기
# bronze 2
import sys

n = int(sys.stdin.readline())

primes = list(map(int, sys.stdin.readline().split()))


def is_prime(_num):
    if _num == 1: return False
    if _num == 2: return True
    for i in range(2, (int(_num / 2)) + 1):
        if _num % i == 0:
            return False

    return True


count = 0

for num in primes:
    if is_prime(num):
        count += 1
print(count)
