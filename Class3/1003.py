def fibo(n):
    dp = [0] * (n+1)
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    dp[0] = 0
    dp[1] = 1
    
    zero =[]
    one = []
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

global zero
zero = 0
global one
one = 0
def custom_fibo(n):
    global zero , one
    if n == 0:
        zero += 1
        return 0
    elif n == 1:
        one += 1
        return 1
    else: return custom_fibo(n-1) + custom_fibo(n-2)

def cal_zero_one(n):
    zero = 1
    one = 0
    dp = [0] * (n+1)
    dp[0] = [zero , one]
    for i in range(1,n+1):
        dp[i] = [dp[i-1][1] , sum(dp[i-1])]
    return dp[n]
    
    
# for i in range(1,30):
#     zero,one = 0 , 0
#     custom_fibo(i)
#     print(zero,one)
import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    num = int(sys.stdin.readline().strip())
    print(*cal_zero_one(num))