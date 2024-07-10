# https://www.acmicpc.net/problem/1629
# 곱셈
# silver 1
# re
import sys


# 나머지 분배의 법칙을 알아야 풀 수 있음. ab % c = {(a % c) * (b % c)} % c
def mod_dist_law(a, b, c):
    if b == 1:
        return a % c
    k = mod_dist_law(a, b // 2, c)
    if b % 2 == 0:
        return (k * k) % c
    return (k * k * a) % c


a, b, c = map(int, sys.stdin.readline().split())

print(mod_dist_law(a, b, c))
