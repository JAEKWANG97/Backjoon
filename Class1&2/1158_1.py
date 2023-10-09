import sys


n = int(sys.stdin.readline())

arr = []

k = int(sys.stdin.readline())

for i in range(0, n):
    arr.append(int(i))

new_arr = []

while len(arr) > 0:
    new_arr.append(arr.pop(k+1))

    if len(arr) < k:
        k = (k + k) % len(arr) + 1
    else:
        k = k + k

print(new_arr)

