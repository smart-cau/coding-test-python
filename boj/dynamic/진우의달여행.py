# https://www.acmicpc.net/problem/17484
# 진우의 달 여행(Small)
# silver 3
# re
import sys

row, col = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(row)]

# DP 배열 초기화 (행, 열, 이전 이동 방향)
# 이전 이동 방향: 0 - 왼쪽 대각선, 1 - 수직, 2 - 오른쪽 대각선
dp = [[[float('inf')] * 3 for _ in range(col)] for _ in range(row)]

# 첫 번째 행 초기화
for j in range(col):
    for d in range(3):
        dp[0][j][d] = fuel[0][j]

# DP 진행
for i in range(1, row):
    for j in range(col):
        for d in range(3):
            if d == 0 and j > 0:  # 왼쪽 대각선
                dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + fuel[i][j]
            if d == 1:  # 수직
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + fuel[i][j]
            if d == 2 and j < col-1:  # 오른쪽 대각선
                dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + fuel[i][j]

# 마지막 행에서 최소값 찾기
result = min(min(dp[row-1][j]) for j in range(col))
print(result)