# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# silver 2
import sys

input = sys.stdin.readline

seq_size = int(input().rstrip())
seqs = list(map(int, input().rstrip().split()))
ordered_unique_seq = sorted(list(set(seqs)))

dp = [[0] * (seq_size + 1) for _ in range(len(ordered_unique_seq) + 1)]

for i in range(1, len(ordered_unique_seq) + 1):
    for j in range(1, seq_size + 1):
        if ordered_unique_seq[i - 1] == seqs[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(ordered_unique_seq)][seq_size])
