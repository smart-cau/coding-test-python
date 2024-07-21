# https://www.acmicpc.net/problem/1931
# 회의실 배정
# silver 1
# re
import sys

conf_room_time_count = int(sys.stdin.readline())

times = []

for _ in range(conf_room_time_count):
    start, end = map(int, sys.stdin.readline().split())
    times.append([start, end])

times.sort(key=lambda x: (x[1], x[0]))

count = 1
end = times[0][1]

for i in range(1, conf_room_time_count):
    if times[i][0] >= end:
        count += 1
        end = times[i][1]

print(count)
