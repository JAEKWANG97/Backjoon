# 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.

# 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

#  N개보다 많이 만드는 것도 N개를 만드는 것에 포함

# 4 11
# 802
# 743
# 457
# 539


import sys
import time

str = list(sys.stdin.readline().strip().split(' '))
n = int(str[0])
m = int(str[1])
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

a = sum(arr) // m
b = 0

# 기준선을 정해서 2분법
# 길이가 a인 랜선으로 자르는데 value가 m보다 클 경우, a가 작다는걸 의미
# 길이가 a인 랜선으로 자르는데 value가 m보다 작을 경우, a가 크다는걸 의미

# a가 작다면,    2a
# a가 크다면,   a//2

# min 값과 max 값이 있어야 함
# min은 (전체 길이 // m+1)
# max는 (전체 길이 // m-1)

min_value = 1
max_value = max(arr)
a = (min_value + max_value) //2
while min_value <= max_value:
    value = 0
    for i in range(n):
        value += arr[i] // a
    if value >= m: 
        min_value = a + 1
        a = (min_value + max_value) // 2
    else:  
        max_value = a - 1
        a = (min_value + max_value) // 2


print(a)
        
