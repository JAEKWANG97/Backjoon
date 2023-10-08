# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

import sys

n = int(sys.stdin.readline().strip())
arr = dict()

min_value = float('inf')
max_value = 0
for i in range(n):
    str = list(map(int,list(sys.stdin.readline().strip().split(' '))))
    n , m = str[0] , str[1]
    if n not in arr:
        arr[n] = []
    arr[n].append(m)
    if n > max_value:
        max_value = n
    if n < min_value:
        min_value = n

for i in range(min_value , max_value+1):
    if i in arr:
        arr[i] = sorted(arr[i])
        for j in arr[i]:
            print(i , j)

        
