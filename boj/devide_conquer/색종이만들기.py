# https://www.acmicpc.net/problem/2630
# 색종이 만들기
# silver 2
import sys


def is_same_color(papers):
    if len(papers) == 1:
        return True
    l = len(papers)
    for i in range(l):
        for j in range(l):
            if papers[0][0] != papers[i][j]:
                return False
    return True


def cut_paper(paper, colors):
    l = len(paper)
    color = paper[0][0]
    if is_same_color(paper):
        if color == 0: colors[0] += 1
        if color == 1: colors[1] += 1
        return

    mid = l // 2

    top_left = [row[:mid] for row in paper[:mid]]
    top_right = [row[mid:] for row in paper[:mid]]
    bottom_left = [row[:mid] for row in paper[mid:]]
    bottom_right = [row[mid:] for row in paper[mid:]]

    cut_paper(top_left, colors)
    cut_paper(top_right, colors)
    cut_paper(bottom_left, colors)
    cut_paper(bottom_right, colors)


N = int(sys.stdin.readline())

init_papers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

colors = [0 for _ in range(2)]

cut_paper(init_papers, colors)

print(*colors, sep='\n')
