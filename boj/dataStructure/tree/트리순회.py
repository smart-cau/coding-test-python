# https://www.acmicpc.net/problem/1991
# 트리순회
# silver 1
import sys


class TreeNode:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_helper(temp: TreeNode, parent: str, left: str, right: str):
    if temp.val == parent:
        temp.left = None if left == '.' else TreeNode(left)
        temp.right = None if right == '.' else TreeNode(right)
        return
    if temp.left is not None:
        build_tree_helper(temp.left, parent, left, right)
    if temp.right is not None:
        build_tree_helper(temp.right, parent, left, right)


def preorder(node: TreeNode, result):
    if node is not None:
        result.append(node.val)
        preorder(node.left, result)
        preorder(node.right, result)


def inorder(node: TreeNode, result):
    if node is not None:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)


def postorder(node: TreeNode, result):
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.val)


tree_size = int(sys.stdin.readline())
root = TreeNode('A') # tree.

for _ in range(tree_size):
    parent, left, right = sys.stdin.readline().split()
    build_tree_helper(root, parent, left, right)


pre_result = []
in_result = []
post_result = []
preorder(root, pre_result)
inorder(root, in_result)
postorder(root, post_result)
print(*pre_result, sep='')
print(*in_result, sep='')
print(*post_result, sep='')
