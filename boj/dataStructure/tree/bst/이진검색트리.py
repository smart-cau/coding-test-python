# https://www.acmicpc.net/problem/5639
# 이진 검색 트리
# gold 4
import sys

sys.setrecursionlimit(10 ** 7)


def postorder(subtree, result):
    if len(subtree) == 0:
        return

    root_idx = 0
    left_idx = 1
    right_idx = None
    size = len(subtree)
    for i in range(1, len(subtree)):
        if subtree[i] > subtree[root_idx]:
            right_idx = i
            break
    right_idx = right_idx if right_idx is not None else size
    # left subtree
    postorder(subtree[left_idx:right_idx], result)
    # right subtree
    postorder(subtree[right_idx:size], result)
    # root
    result.append(subtree[root_idx])


nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


result = []
postorder(nums, result)

print(*result, sep='\n')
