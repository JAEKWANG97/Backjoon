import sys

n = sys.stdin.readline()

arr = list(map(int, sys.stdin.readline().split()))

sorted_arr = sorted(arr)

for x in arr:
    print(sorted_arr.index(x), end=' ')
