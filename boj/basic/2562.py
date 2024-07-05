import sys

# 입력 받기
nums = [int(sys.stdin.readline()) for _ in range(9)]

# 최대값과 해당 인덱스 찾기
max_num, max_index = max((num, i) for i, num in enumerate(nums, start=1))

# 결과 출력
print(max_num)
print(max_index)