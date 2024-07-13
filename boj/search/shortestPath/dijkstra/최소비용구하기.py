# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
# gold 5
import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 1e9
distances = [INF] * (N + 1)
cities = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    cities[start].append([weight, end])

origin, destination = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))  # (우선순위, 값)의 형태

    while q:
        current_dist, current = heapq.heappop(q)

        if current_dist > distances[current]:
            continue

        neighbors = cities[current]
        for weight, neighbor in neighbors:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))

    return distances


distances = dijkstra(origin)
print(distances[destination])
