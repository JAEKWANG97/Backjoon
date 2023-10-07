# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merge_arr.append(right[j])
            j += 1
        else:
            merge_arr.append(left[i])
            i += 1
    merge_arr = merge_arr + left[i:]
    merge_arr = merge_arr + right[j:]

    return merge_arr


for x in merge_sort(arr):
    print(x)
