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

# 불리언 배열을 이요해야함 인덱스를 활용해서

value = math.sqrt(m)

def search_decimal(m):
    decimal = []
    for i in range(m):
        if decimal[i] < value:
            if value % decimal != 0:
