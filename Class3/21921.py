import sys

n, x = map(int, input().split())
visitant = list(map(int, sys.stdin.readline().strip().split()))

max_sum = sum(visitant[:x])
current_sum = max_sum
count = 0 if max_sum == 0 else 1

for i in range(1, n - x + 1):
    current_sum = current_sum - visitant[i-1] + visitant[i+x-1]
    
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum > 0:
    print(max_sum)
    print(count)
else:
    print('SAD')
