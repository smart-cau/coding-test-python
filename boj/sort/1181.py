# https://www.acmicpc.net/problem/1181
# 단어 정렬
# silver 5
import sys

count = int(sys.stdin.readline())

words = {sys.stdin.readline().strip() for _ in range(count)}

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
