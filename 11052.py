
n = int(input())
p = [0] + list(map(int, input().split()))  # 0번째 인덱스를 사용하지 않기 위해 0을 추가

dp = [0] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i] , dp[i-j] + p[j])

print(dp[n])