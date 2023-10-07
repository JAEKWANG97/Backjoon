# 백준 2164 의 다른 풀이

# 2의 n승과 x 를 비교하는 로직

# 2의 n승을 표현하기 위해 비트연산자를 사용

import sys

n = int(sys.stdin.readline())
 
def isPowerOf2(n : int) -> bool:
    return (n&(n-1))==0

def leftmost_one_position(n: int) -> int:
    return 2 ** (n.bit_length() - 1)

if isPowerOf2(n):
    print(n)
else:
    print( (n -leftmost_one_position(n) )* 2)