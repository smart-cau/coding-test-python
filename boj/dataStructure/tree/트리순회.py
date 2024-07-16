# https://www.acmicpc.net/problem/1991
# 트리순회
# silver 1
import sys


def preorder(node: str, result):
    if node != '.':
        result.append(node)
        preorder(tree[node][0], result)
        preorder(tree[node][1], result)


def inorder(node: str, result):
    if node != '.':
        inorder(tree[node][0], result)
        result.append(node)
        inorder(tree[node][1], result)


def postorder(node: str, result):
    if node != '.':
        postorder(tree[node][0], result)
        postorder(tree[node][1], result)
        result.append(node)


tree_size = int(sys.stdin.readline())
tree = {}

for _ in range(tree_size):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = [left, right]


pre_result = []
in_result = []
post_result = []
preorder('A', pre_result)
inorder('A', in_result)
postorder('A', post_result)
print(*pre_result, sep='')
print(*in_result, sep='')
print(*post_result, sep='')
