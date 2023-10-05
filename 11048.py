# 준규는 N×M 크기의 미로에 갇혀있다. 
# 미로는 1×1크기의 방으로 나누어져 있고, 
# 각 방에는 사탕이 놓여져 있다. 
# 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.

# 준규는 현재 (0, 0)에 있고, (N-1, M-1)으로 이동하려고 한다. 
# 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고,
# 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 또, 미로 밖으로 나갈 수는 없다.

# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

import sys
str = sys.stdin.readline().rstrip().split(' ')
n = int(str[0])
m = int(str[1])

# 1 2 3 4
# 0 0 0 5
# 9 8 7 6
dp = [[0] * (m)] * (n)


for i in range(n):
    str = sys.stdin.readline().rstrip().split(' ')
    dp[i] =  list(map(int, str))



max_candy = [[0] * (m+1)] * (n+1)
max_candy[0][0] = dp[0][0]
# max_candy[1][0] = dp[1][0] + dp[0][0]
# max_candy[0][1] = dp[0][1] + dp[0][0]


for i in range(0,n):
    for j in range(0,m):
        if i> 0 or j > 0:
            value = max(max_candy[i-1][j] , max_candy[i][j-1], max_candy[i-1][j-1])
            max_candy[i][j] = value + dp[i][j]
print(max_candy[n-1][m-1])