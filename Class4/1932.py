import sys

n = int(input())

lines = sys.stdin.readlines()
arr = []
for i in range(len(lines)):
    arr.append(list(map(int, lines[i].split())))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(len(arr[i])):
        if i == 0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + arr[i][j]

print(max(dp[n - 1]))
