# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5
import sys
n , m  = map(int, sys.stdin.readline().strip().split(' '))

arr = list(map(int,sys.stdin.readline().strip().split(' ')))



def dp_table(arr,n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
        # 길이가 1인 부분 배열
    for i in range(n):
        dp[i][i] = arr[i]
    
    # 길이가 2인 부분 배열
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
    
    for length in range(3,n):
        for i in range(n - length ):
            j = i + length - 1
            dp[i][j] = dp[i][j-1] + arr[j]
    
    return(dp)
dp = dp_table(arr,n)
for _ in range (m):
    i , j  = map(int, sys.stdin.readline().strip().split(' '))
    print(dp[i-1][j-1])
    