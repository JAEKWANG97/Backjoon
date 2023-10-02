# m 개 중 n 개를 고르는 조합

# mCn

# nCr = n! / r!(n-r)!

#팩토리 구현 문제

# N, M (0 < N ≤ M < 30)

# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.
import sys

def factorial(num):
    # dp = [0] * (num + 1)
    # dp[0] = 0
    # if num == 0 : return 0
    # dp[1] = 1
    # if num == 1 : return 1

    # for i in range(2,num+1):
    #     dp[i] = dp[i-1] * i

    # return dp[num]
    temp = 1
    for i in range(1,num+1):
        temp = temp * i

    return int(temp)

def combination(n : int , r : int) -> int :
    if n-r == 0 : return 1
    return factorial(n) / (factorial(r) * factorial(n-r))

T = int(input())
for _ in range(T):
    str = sys.stdin.readline().rstrip().split(' ')
    n = int(str[0])
    m = int(str[1])
    print(combination(m,n))