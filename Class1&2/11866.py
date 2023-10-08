# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

import sys

str = list(map(int,list(sys.stdin.readline().strip().split())))
n , m = str[0] , str[1]

arr = [x for x in range(1,n+1)]

pointer = 0

answer = []

while len(arr) > 1:
    pointer += m - 1
    while pointer >= len(arr):
        pointer -= len(arr)
    answer.append(arr.pop(pointer))


print('<' , end="")
for x in answer:
    print(x , end=", ")
print(arr.pop() , end="")
print('>')    
