# 에라토스테네스의체

# 1~n 까지의 수가 있다.
# 2를 남기고 나머지 제거
# 3을 남기고 나머지 제거 
# ....
# ....
# 소수 완성!



import sys
import math
str = list(map(int, list(sys.stdin.readline().strip().split(' '))))
n , m = str[0] , str[1]

arr = [x for x in range(1,int(m)+1)]

value = math.sqrt(m)

def search_decimal(m):
    decimal = []

    if m < 2:
        return
    decimal.append(2)    
    for i in range(3,m+1):
        value=True  
        for x in decimal:
            if x * x > i:
                break
            if i % x == 0:
                value = False
                break
        if value:
            decimal.append(i)
    return decimal

decimal = search_decimal(m)
result = [x for x in decimal if x >= n]
for x in result:
    print(x)

