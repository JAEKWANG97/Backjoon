# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

import sys

str = list(sys.stdin.readline().strip().split(' '))
n = int(str[0])
m = int(str[1])

def getDivisor(n : int):
    arr = set()
    for i in range(1, int(round(n**0.5)) + 1):
        if n % i == 0:
            arr.add(int(i))
            arr.add(int(n/i))
    return arr

def get_gcd(n, m):
    n_divisor = getDivisor(n)
    m_divisor = getDivisor(m)
    
    #intersection 함수는 set 에서 제공하는 함수로 교집합을 반환함
    common_divisors = n_divisor.intersection(m_divisor)
    
    if common_divisors:
        return max(common_divisors)
    else:
        return 1  # 모든 정수의 약수는 최소한 1입니다.

def get_lcm(n,m):
    return n * m // get_gcd(n,m)

print(get_gcd(n,m))
print(get_lcm(n,m))