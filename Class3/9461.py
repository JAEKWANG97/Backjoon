# 파도 수열 

# i번째를 구하기 위해  i-2 와 i-3의 합

def dp():
    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,101):
        dp[i] = dp[i-2] + dp[i-3]
    
    return dp


import sys

dp= dp()
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(dp[n])

# for i in range(10):
#     print(dp[i+1])