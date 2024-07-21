# https://www.acmicpc.net/problem/1700
# 멀티탭 스케쥴링
# gold 1
# re
plug_count, uses_count = map(int, input().split(' '))
uses = list(map(int, input().split(' ')))
using_plugs = []
count = 0
MAX_VALUE = 101

for idx in range(uses_count):
    current = uses[idx]
    if current in using_plugs :  # 코드에 이미 꽂혀져있음
        continue
    if len(using_plugs) < plug_count :  # 코드 자리 남음
        using_plugs.append(current)
        continue

    priority = []
    for plug in using_plugs:  # 꽂혀져 있는 코드들
        if plug in uses[idx:]: # 다음에 또 이용해야한다면
            priority.append(uses[idx:].index(plug))
        else:
            priority.append(MAX_VALUE)
    target = priority.index(max(priority))
    using_plugs.remove(using_plugs[target])
    using_plugs.append(current)
    count += 1

print(count)