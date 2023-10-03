import sys
str = sys.stdin.readline().rstrip().split(' ')
n = int(str[0])
m = int(str[1])

dp = [[0] * (m) for _ in range(n)]

for i in range(n):
    str = sys.stdin.readline().rstrip().split(' ')
    dp[i] = list(map(int, str))

# `max_candy` 2차원 리스트를 올바르게 초기화
max_candy = [[0] * (m) for _ in range(n)]
max_candy[0][0] = dp[0][0]

for i in range(0, n):
    for j in range(0, m):
        if i > 0:
            max_candy[i][j] = max(max_candy[i][j], max_candy[i-1][j] + dp[i][j])
        if j > 0:
            max_candy[i][j] = max(max_candy[i][j], max_candy[i][j-1] + dp[i][j])
        if i > 0 and j > 0:
            max_candy[i][j] = max(max_candy[i][j], max_candy[i-1][j-1] + dp[i][j])

print(max_candy[n-1][m-1])
