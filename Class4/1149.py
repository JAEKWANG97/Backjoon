import sys

n = int(input())
lines = sys.stdin.readlines()
dp = [[0] * 3 for _ in range(n)]
arr = []
for line in lines:
    nums = list(map(int, line.split()))
    arr.append(nums)

for i in range(n):
    for j in range(3):
        if i == 0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + arr[i][j]

print(min(dp[n-1]))
