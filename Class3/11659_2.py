# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5
import sys
n , m  = map(int, sys.stdin.readline().strip().split(' '))

arr = list(map(int,sys.stdin.readline().strip().split(' ')))

Prefix_arr = []

for x in arr:
    if len(Prefix_arr) >0:
        Prefix_arr.append(x+Prefix_arr[-1])
    else:
        Prefix_arr.append(x)
# 누적합 A~B 까지 누적합을 구한다음
# i,j의 누적합은 누적합 [j] -  누적합 [i - 1]

# 하.......
for _ in range (m):
    i , j  = map(int, sys.stdin.readline().strip().split(' '))
    if i > 1:
        print(Prefix_arr[j-1] - Prefix_arr[i-2])
    else:
        print(Prefix_arr[j-1])
    