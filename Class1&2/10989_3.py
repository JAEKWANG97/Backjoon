import sys

n = int(sys.stdin.readline().strip())

min_value = float('inf')
max_value = 0
arr = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if max_value < num: 
        max_value = num
    if min_value > num:
        min_value = num
    arr.append(num)

count = [0] * (max_value - min_value + 1)

for i in arr:
    count[i - min_value] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1] 

sorted_arr = [0] * n
for i in range(len(arr)-1, -1 , -1):
    sorted_arr[count[arr[i] - min_value] - 1] = arr[i]
    count[arr[i] - min_value] -= 1

print(sorted_arr)
