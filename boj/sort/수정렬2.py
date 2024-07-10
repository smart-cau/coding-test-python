# https://www.acmicpc.net/problem/2751
# 수 정렬2
# silver 5
import sys

sys.setrecursionlimit(10 ** 6)


# 퀵 정렬 최악의 case인 경우 시간복잡도는 n^2. 해결하기 위해선 pivot을 랜덤으로 잡아야 함.
# 따라서 최악의 경우에도 nlogn을 보장하는 merge sort 적용
def merge_sort(arr):
    # 가장 잘개 쪼개진 경우. devided
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []

    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


def merge_sort_optimized(arr):
    # 보조 함수: 실제 정렬 수행
    def sort(low, high):
        if high - low <= 1:
            return

        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    # 보조 함수: 두 정렬된 부분 배열 병합
    def merge(low, mid, high):
        arr_left = arr[low:mid]
        arr_right = arr[mid:high]

        l, h, k = 0, 0, low

        while l < len(arr_left) and h < len(arr_right):
            if arr_left[l] <= arr_right[h]:
                arr[k] = arr_left[l]
                l += 1
            else:
                arr[k] = arr_right[h]
                h += 1
            k += 1

        # 남은 부분 복사
        while l < len(arr_left):
            arr[k] = arr_left[l]
            l += 1
            k += 1

        while h < len(arr_right):
            arr[k] = arr_right[h]
            h += 1
            k += 1

    # 메인 정렬 함수 호출
    sort(0, len(arr))


N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]

merge_sort_optimized(numbers)

print(*numbers, sep='\n')
