# https://www.acmicpc.net/problem/2805
# 나무 자르기
# silver 2
# re
import sys

N, M = map(int, sys.stdin.readline().split())

max_h = 0
tree_heights = []

inputs = map(int, sys.stdin.readline().split())

for tree in inputs:
    if tree > max_h: max_h = tree
    tree_heights.append(tree)


def cut_woods(trees, height):
    woods = 0
    for tree in trees:
        if tree > height:
            woods += (tree - height)
    return woods


def binary_search(trees):
    left, right = 0, max_h

    while True:
        height = (left + right) // 2
        # 틀린 1번째 이유. 종료조건을 위로 써야함
        if left > right:
            return height
        # 2번째 이유. 최대값을 구하기 위해 구하고자 하는 높이가 같더라도 한번 더 높은 값을 검색해야 함
        if M <= cut_woods(trees, height):
            left = height + 1
        if M > cut_woods(trees, height):
            right = height - 1


print(binary_search(tree_heights))
