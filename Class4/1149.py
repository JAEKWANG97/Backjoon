import sys

n = int(input())
lines = sys.stdin.readlines()
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    num = list(map(int, lines[i].split()))
    for j in range(3):
        if i == 0:
            dp[i][j] = num[j]
        else:
            dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + num[j]

print(min(dp[n - 1]))
