# https://www.acmicpc.net/problem/11047
# 동전 0
# silver 4
import sys

coin_types, total_amount = map(int, sys.stdin.readline().split())

types_of_coins = []

for _ in range(coin_types):
    types_of_coins.append(int(sys.stdin.readline().strip()))

max_coin_idx = 0

for i in range(coin_types):
    max_coin_idx = i
    if types_of_coins[i] > total_amount:
        break

total_coins = 0
for i in range(max_coin_idx, -1, -1):
    coin = total_amount // types_of_coins[i]
    total_coins += coin
    total_amount -= coin*types_of_coins[i]
    if total_amount == 0:
        break

print(total_coins)
