import sys 

t = int(sys.stdin.readline().strip())
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# dp를 활용해서 푸는 문제임, 구하고자하는 수 == sum(fun(n - 1), fun(n -2) , fun(n -3))
dp= [0] * (11+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11+1):
    dp[i] = sum([dp[i-1] , dp[i-2] , dp[i-3]])
        
    




for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(dp[n])