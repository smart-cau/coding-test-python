# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
# bronze 1
import sys

all_dwarfs = [int(sys.stdin.readline().strip()) for _ in range(9)]
total_height = sum(all_dwarfs)

temp1 = temp2 = 0


def find_thieves(dwarfs):
    thieves = []
    for i in range(len(dwarfs) - 1):
        for j in range(i + 1, len(dwarfs)):
            if total_height - all_dwarfs[i] - all_dwarfs[j] == 100:
                thieves.append(all_dwarfs[i])
                thieves.append(all_dwarfs[j])
                return thieves


thieves = find_thieves(all_dwarfs)
all_dwarfs.remove(thieves[0])
all_dwarfs.remove(thieves[1])
all_dwarfs.sort()

print(*all_dwarfs, sep='\n')
