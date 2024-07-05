# https://www.acmicpc.net/problem/9020
# 골드바흐의 추측
# silver 2
import sys

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(n)]

# sieve of eratostheses
def eratos(num: int) -> list:
    sieve = [False] * (num + 1)
    sieve[0] = sieve[1] = True
    result = []
    for i in range(2, num + 1):
        if not sieve[i]:
            result.append(i)
            j = 1
            while (i * j) <= num:
                sieve[i * j] = True
                j += 1

    return result

# goldbach partition
for num in nums:
    primes = eratos(num)
    results = []
    min = sys.maxsize
    for prime in primes:
        res = num - prime
        if res in primes and abs(prime - res) < min:
            min = abs(prime - res)
            results = [prime, res]

    print(*results)

