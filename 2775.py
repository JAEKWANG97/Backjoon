import sys

T = int(sys.stdin.readline())
#  0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다

#  a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 2 층의 3호 ==> 1 2 3 ,  1 3 6 , 1 4 10 

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    rows, cols = k, n
    dp = [[0] * n for _ in range(k+1)]
    
    for i in range(n):
        dp[0][i] = i+1
    
    for i in range(1, k+1):
        for j in range(0,n):
            dp[i][j] = sum(dp[i-1][:j+1]) 
    
    print(dp[k][n-1])

    

